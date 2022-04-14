import numpy as np
import pickle
from collections import Counter

from utils import normalize_text


class DataLoader:

    def __init__(self):
        pass

    def load_data(self, path):
        data = []
        with open(path, "r", encoding="utf-8") as f:
            label = path.split("/")[-1]
            label = label[:-4]
            for line in f:
                if line.strip():
                    if len(line) >= 150:
                        data.append((line.strip(), label))
        return data


# if __name__ == "__main__":
#     data_loader = DataLoader()
#     data = data_loader.load_data("data/sports.txt")
#     print(data[-1], normalize_text(data[-1][0], use_tokenize=True))