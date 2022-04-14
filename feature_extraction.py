from collections import Counter
import numpy as np


def _gen_ngram_from_text(text, n):
    words = text.split()
    L = len(words)
    ngrams = []
    if n < 1 or words is None:
        return None
    for i in range(0, L - n + 1):
        try:
            ngrams.append("_".join(token for token in words[i: i + n]))
        except:
            continue
    return ngrams


class TfidfTransform:

    def __init__(self, ngram_range=(1, 1), stop_word=None, vocab=None) -> None:
        if stop_word is None:
            self.stop_word = []
        else:
            self.stop_word = stop_word
        self.min_gram = ngram_range[0]
        self.max_gram = ngram_range[-1]
        if vocab is None:
            self.vocab = dict()
        else:
            self.vocab = self.vocab
    
    def fit(self, X):
        idx = 0
        for sent in X:
            tokens = []
            if self.min_gram < self.max_gram:
                for n in range(self.min_gram, self.max_gram + 1):
                    tokens += _gen_ngram_from_text(sent, n)
            else:
                tokens = _gen_ngram_from_text(sent, self.min_gram)
            for token in tokens:
                if token in self.vocab or token in self.stop_word:
                    continue
                else:
                    self.vocab[token] = {"id": idx, "idf": 0}
                    idx += 1
        N = len(X)
        for i, sent in enumerate(X):
            tokens = []
            if self.min_gram < self.max_gram:
                for n in range(self.min_gram, self.max_gram + 1):
                    tokens += _gen_ngram_from_text(sent, n)
            else:
                tokens = _gen_ngram_from_text(sent, self.min_gram)
            tokens = Counter(sent)
            for token in tokens:
                if token in self.vocab:
                    self.vocab[token]["idf"] += 1
                else:
                    continue
        for token in self.vocab:
            self.vocab[token]["idf"] = np.log10(N / (self.vocab[token]["idf"] + 1))
            if self.vocab[token]["idf"] < 0:
                self.vocab[token]["idf"] = 0
        return self
    

    def transform(self, X):
        X_new = np.zeros((len(X), len(self.vocab)))
        for i, sent in enumerate(X):
            tokens = []
            if self.min_gram < self.max_gram:
                for n in range(self.min_gram, self.max_gram + 1):
                    tokens += _gen_ngram_from_text(sent, n)
            else:
                tokens = _gen_ngram_from_text(sent, self.min_gram)
            tokens = Counter(tokens)
            for token in tokens:
                if token in self.vocab:
                    X_new[i][self.vocab[token]["id"]] = tokens[token] * self.vocab[token]["idf"] / len(tokens)
        return X_new


class CountVectorizer:

    def __init__(self, ngram_range=(1, 1), stop_word=None, vocab=None) -> None:
        if stop_word is None:
            self.stop_word = []
        else:
            self.stop_word = stop_word
        self.min_gram = ngram_range[0]
        self.max_gram = ngram_range[-1]
        if vocab is None:
            self.vocab = dict()
        else:
            self.vocab = self.vocab
    
    def fit(self, X):
        idx = 0
        for sent in X:
            tokens = []
            if self.min_gram < self.max_gram:
                for n in range(self.min_gram, self.max_gram + 1):
                    tokens += _gen_ngram_from_text(sent, n)
            else:
                tokens = _gen_ngram_from_text(sent, self.min_gram)
            for token in tokens:
                if token in self.vocab or token in self.stop_word:
                    continue
                else:
                    self.vocab[token] = idx
                    idx += 1
        return self
    

    def transform(self, X):
        X_new = np.zeros((len(X), len(self.vocab)))
        for i, sent in enumerate(X):
            tokens = []
            if self.min_gram < self.max_gram:
                for n in range(self.min_gram, self.max_gram + 1):
                    tokens += _gen_ngram_from_text(sent, n)
            else:
                tokens = _gen_ngram_from_text(sent, self.min_gram)
            tokens = Counter(tokens)
            for token in tokens:
                if token in self.vocab:
                    X_new[i][self.vocab[token]] = tokens[token]
        return X_new