"""Unittest for src.data.make_dataset.split_train_val_data"""

import unittest
from unittest import mock
import logging
import pandas as pd

import src
from tests import str_generator
from src.data import split_train_val_data
from src.entities import SplittingParams, DatasetParams

# switch off import-logging
logging.getLogger(src.data.make_dataset.__name__).disabled = True


class TestSplitTrainValData(unittest.TestCase):
    """Tests for split_train_val_data"""

    def test_split_train_val_data(self):
        """Should test splitting to train/val"""
        for row_size in [5, 10, 25]:
            dataframe = pd.DataFrame([list(str_generator(5)) for _ in range(row_size)])
            # mock dataclasses
            split_mock = SplittingParams(0.2, 13)
            dataset_mock = DatasetParams("nn.csv", ["test.csv", "val.csv"])

            with mock.patch("pandas.DataFrame.to_csv") as to_csv_mock:
                test_df, val_df = split_train_val_data(
                    dataframe, split_mock, dataset_mock
                )
                to_csv_mock.assert_has_calls(
                    [mock.call("test.csv"), mock.call("val.csv")], any_order=False
                )
            self.assertEqual(test_df.shape[0], int(0.8 * row_size))
            self.assertEqual(val_df.shape[0], int(0.2 * row_size))


if __name__ == "__main__":
    unittest.main()
