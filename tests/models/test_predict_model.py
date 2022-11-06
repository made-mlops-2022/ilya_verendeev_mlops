"""Unittest for src.data.models.predict_model.predict_model"""

import unittest
import logging
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import src
from src.models import predict_model
from tests import str_generator, int_generator

# constants
COLUMNS_SIZE = 6
ROWS_SIZE = 10
ITERS = 5

# switch off import-logging
logging.getLogger(src.models.predict_model.__name__).disabled = True


class TestPredictModel(unittest.TestCase):
    """Tests for predict_model"""

    def test_predict_model(self):
        """Should test predict model"""

        column_size = 5
        model = RandomForestClassifier()
        columns = list(str_generator(column_size))
        train_df = pd.DataFrame(
            [list(int_generator(column_size)) for _ in range(5)], columns=columns
        )
        target_df = pd.Series(
            [list(int_generator(1))[0] for _ in range(5)], name=str_generator(1)
        )
        model.fit(train_df, target_df)

        for row_size in [5, 10, 15]:

            dataframe = pd.DataFrame(
                [list(int_generator(column_size)) for _ in range(row_size)],
                columns=columns,
            )
            self.assertEqual(row_size, predict_model(model, dataframe).shape[0])


if __name__ == "__main__":
    unittest.main()
