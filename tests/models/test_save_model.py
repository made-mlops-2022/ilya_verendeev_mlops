"""Unittest for src.data.features.build_features.extract_target"""

import unittest
from unittest import mock
import logging
from sklearn.ensemble import RandomForestClassifier
import src
from src.entities import ModelParams
from src.models import save_model

# constants
COLUMNS_SIZE = 6
ROWS_SIZE = 10
ITERS = 5

# switch off import-logging
logging.getLogger(src.models.train_model.__name__).disabled = True


class TestSaveModel(unittest.TestCase):
    """Tests for save_model"""

    def test_save_model(self):
        """Should save model to file"""

        with mock.patch("builtins.open") as to_csv_mock:

            model_mock = ModelParams(
                model_name="RandomForestClassifier",
                parameters=[],
                model_save_path="test.pkl",
            )

            model = RandomForestClassifier()
            save_model(model, model_params=model_mock)
            to_csv_mock.assert_called_with("test.pkl", "wb")
            self.assertTrue(isinstance(model, RandomForestClassifier))


if __name__ == "__main__":
    unittest.main()
