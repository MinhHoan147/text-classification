import numpy as np
from sklearn.model_selection import train_test_split
import math
import utils
from datasets import DataLoader
from feature_extraction import CountVectorizer, TfidfTransform
from sklearn.metrics import accuracy_score
import pickle

class MultinomialNB():
    def __init__(self, alpha=1.0):
        self.alpha = alpha
        self.__classes = []
        self.prob = None
        self.prob_c = None

    def fit(self, X_train, y_train):
        self.__classes = list(set(y_train))
        count = np.zeros((len(self.__classes), X_train.shape[1]))
        len_class = np.zeros(len(self.__classes))
        self.prob_c = np.zeros(len(self.__classes))
        self.prob = np.zeros((len(self.__classes), X_train.shape[1]))
        for i, c in enumerate(y_train):
            self.prob_c[int(c) - 1] += 1
            len_class[int(c) - 1] += np.sum(X_train[i])
            count[int(c) - 1] += X_train[i]
        self.prob_c = self.prob_c/X_train.shape[0]
        for c in self.__classes:
            self.prob[int(c) - 1] = (count[int(c) - 1] + self.alpha)/(len_class[int(c) - 1] + self.alpha*X_train.shape[1])


    def predict(self, X_test):
        y_pred = []
        for i in range(X_test.shape[0]):
            _max = -99999.0
            _c = 0
            for c in self.__classes:
                _prob = math.log(self.prob_c[int(c) - 1])
                for j in range(X_test.shape[1]):
                    if X_test[i][j] != 0:
                        _prob += math.log(self.prob[int(c) - 1][j])*X_test[i][j]
                if _prob > _max:
                    _max = _prob
                    _c = c
            y_pred.append(_c)
        return y_pred

    def accuracy(self, y_test, y_pred):
        count = 0
        for i in range(len(y_test)):
            if str(y_test[i]) == str(y_pred[i]):
                count += 1
        print('Acc: %.2f' % (count*100/len(y_test)), end=' %')


if __name__ == '__main__':
    data_loader = DataLoader()
    sports = data_loader.load_data("data/sports.txt")
    education = data_loader.load_data("data/education.txt")
    heathy = data_loader.load_data("data/heathy.txt")
    finance = data_loader.load_data("data/finance.txt")
    data = sports + education + heathy + finance
    X = []
    y = []
    for content in data:
        X.append(utils.normalize_text(content[0]))
        if content[-1] == "sports":
            y.append(0)
        elif content[-1] == "education":
            y.append(1)
        elif content[-1] == "heathy":
            y.append(2)
        else:
            y.append(3)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

    stop_words = utils.load_stopword("stopwords.txt")

    model = MultinomialNB()
    bag_of_word_model = CountVectorizer(stop_word=stop_words)
    bag_of_word_model.fit(X_train)

    X_train = bag_of_word_model.transform(X_train)
    X_test = bag_of_word_model.transform(X_test)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(accuracy_score(y_test, y_pred))

    pickle.dump(bag_of_word_model, open("models/BOG_stopwords.pkl", "wb"))
    pickle.dump(model, open("models/naive_bayes_stopwords.pkl", "wb"))