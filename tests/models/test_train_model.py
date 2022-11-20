"""Unittest for src.data.models.train_model.train_model"""

import unittest
import logging
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from tests import str_generator, int_generator
import src
from src.entities import ModelParams
from src.models import train_model

# constants
COLUMNS_SIZE = 6
ROWS_SIZE = 10
ITERS = 5

# switch off import-logging
logging.getLogger(src.models.train_model.__name__).disabled = True


class TestSaveModel(unittest.TestCase):
    """Tests for train_model"""

    def test_save_model(self):
        """Should train model with parameters"""

        row_size = 10
        column_size = 5
        model_mock = ModelParams(
            model_name="RandomForestClassifier",
            parameters=[],
            model_save_path="test.csv",
        )
        dataframe = pd.DataFrame(
            [list(int_generator(column_size)) for _ in range(row_size)],
            columns=str_generator(column_size),
        )
        target = pd.Series(
            [list(int_generator(1))[0] for _ in range(row_size)], name=str_generator(1)
        )
        model = train_model(dataframe, model_params=model_mock, target=target)
        self.assertTrue(isinstance(model, RandomForestClassifier))


if __name__ == "__main__":
    unittest.main()
