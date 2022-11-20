"""Unittest for src.data.features.build_features.extract_target"""

import unittest
import random
import logging
import pandas as pd
from tests import str_generator
import src
from src.entities.features_params import FeatureParams
from src.features.build_features import extract_target


# constants
COLUMNS_SIZE = 6
ROWS_SIZE = 10
ITERS = 5

# switch off import-logging
logging.getLogger(src.features.build_features.__name__).disabled = True


class TestExtractTarget(unittest.TestCase):
    """Tests for extract_target"""

    def test_extract_target(self):
        """Should extract column from dataframe"""

        column_names = list(str_generator(COLUMNS_SIZE))

        for _ in range(ITERS):
            dataframe = pd.DataFrame(
                [list(str_generator(COLUMNS_SIZE)) for _ in range(ROWS_SIZE)], columns=column_names
            )
            rand_col = random.choice(column_names)
            feature_mock = FeatureParams([], [], rand_col)
            data, target = extract_target(dataframe, feature_mock)
            self.assertEqual(target.name, rand_col)
            self.assertEqual(data.shape[1], COLUMNS_SIZE - 1)


if __name__ == "__main__":
    unittest.main()
