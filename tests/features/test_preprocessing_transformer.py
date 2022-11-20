"""Unittest for src.data.features.build_features.preprocessing_dataset"""
import logging
import random
import unittest
import src
from src.entities import PreprocessingParams, FeatureParams
from src.features.build_features import PreprocessingTransformer


ITERS = 5

# switch off import-logging
logging.getLogger(src.features.build_features.__name__).disabled = True


class TestPreprocessingDataset(unittest.TestCase):
    """Tests for PreprocessingTransformer"""

    def test_preprocessing_dataset(self):
        """Should preprocess dataset"""

        operation_list = ["normalization", "polynomial", "k-bins"]

        for _ in range(ITERS):
            left = random.randint(0, len(operation_list) - 1)
            right = random.randint(left + 1, len(operation_list))
            preprocessing_params = PreprocessingParams(operation_list[left:right])
            feature_params = FeatureParams(
                numerical_features=["age", "size"],
                categorical_features=["name", "surname"],
                target_col="class",
            )

            transformer = PreprocessingTransformer(preprocessing_params, feature_params)
            data = transformer.get_params()
            self.assertEqual(
                set(data["total_features"].named_steps.keys()),
                set(operation_list[left:right]),
            )
            assert len(data["total_features"].named_steps) > 0


if __name__ == "__main__":
    unittest.main()
