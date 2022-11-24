import pickle
from random import (randint, choice, uniform)
import pandas as pd


class Pipeline:

    def __init__(self):
        self._transformer = None
        self._model = None

    @property
    def transformer(self):
        return self._transformer
    @transformer.setter
    def transformer(self, transformer):
        self._transformer = transformer

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    def predict(self, X: pd.DataFrame):
        X_tmp = self._transformer.transform(X)
        return self._model.predict(X_tmp)

def get_pipe_from_file(filename: str):
    with open(filename, mode='rb') as file:
        pipe = pickle.load(file)
    return pipe

def generate_dataset(size: int):
    while size > 0:
        yield {
            'age': randint(29, 77),
            'sex': choice([0, 1]),
            'cp': choice([0, 1, 2, 3]),
            'trestbps': randint(94, 200),
            'chol': randint(126, 564),
            'fbs': choice([0, 1]),
            'restecg': choice([0, 1, 2]),
            'thalach': randint(71, 202),
            'exang': choice([0, 1]),
            'oldpeak': round(uniform(0, 6.2), 1),
            'slope': choice([0, 1, 2]),
            'ca': choice([0, 1, 2, 3]),
            'thal': choice([0, 1, 2])
        }
        size -= 1