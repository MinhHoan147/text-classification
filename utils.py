from pickle import load
import string
import re

from ftfy import fix_text
from pyvi.ViTokenizer import tokenize


def load_stopword(path):
    stop_words = set([])
    try:
        with open(path, "r") as f:
            for line in f:
                if line.strip():
                    stop_words.add(line.lower())
                else:
                    continue
    except Exception as e:
        pass
    return stop_words


def remove_duplicate(text):
    text = re.sub(r"([A-Za-z])\1+",lambda m: m.group(1), text)
    return text


def normalize_text(text, use_tokenize=False):
    text = text.strip()
    text = fix_text(text)
    table = str.maketrans({key: None for key in string.punctuation})
    text = text.translate(table)
    text = remove_duplicate(text)
    if use_tokenize:
        text = tokenize(text)
    return text.lower()


def normalize(data):
    for i, c in enumerate(data):
        data[i] = normalize_text(i)
    return data


# if __name__ ==  "__main__":
#     stop_words = load_stopword("stopwords.txt")
#     print(len(stop_words))