"""Unittest for src.entities.*"""

import unittest
from src.entities import (ModelParams, FeatureParams, SplittingParams,
                          DatasetParams, PreprocessingParams)


class TestDataClass(unittest.TestCase):
    """Tests for dataclasses"""

    def test_dataset_params(self):
        """Should test for DatasetParams"""
        input_file = 'test.csv'
        output_files = ['test1.csv', 'test2.csv']

        ds_params = DatasetParams(input_file_path=input_file, output_paths=output_files)
        self.assertEqual(ds_params.input_file_path, input_file)
        self.assertEqual(ds_params.output_paths, output_files)

    def test_feature_params(self):
        """Should test for FeatureParams"""
        cat_cols = ['1', '2', '3']
        num_cols = ['4', '5', '6']
        target_col = '7'

        ft_params = FeatureParams(categorical_features=cat_cols,
                                  numerical_features=num_cols,
                                  target_col=target_col)
        self.assertEqual(ft_params.target_col, target_col)
        self.assertEqual(ft_params.categorical_features, cat_cols)
        self.assertEqual(ft_params.numerical_features, num_cols)

    def test_preprocessing_params(self):
        """Should test for PreprocessingParams"""
        params_list = ['1', '2', '3']
        pp_params = PreprocessingParams(pipeline=params_list)
        self.assertEqual(pp_params.pipeline, params_list)

    def test_model_params(self):
        """Should test for ModelParams"""
        model_save_path = 'test.csv'
        model_name = 'Model'
        parameters = [1, 2, 3]
        sp_params = ModelParams(model_save_path=model_save_path,
                                model_name=model_name,
                                parameters=parameters)
        self.assertEqual(sp_params.model_save_path, model_save_path)
        self.assertEqual(sp_params.model_name, model_name)
        self.assertEqual(sp_params.parameters, parameters)

    def test_splitting_params(self):
        """Should test for SplittingParams"""
        val_size = 0.2
        random_state = None
        sp_params = SplittingParams(val_size=val_size,
                                    random_state=random_state)
        self.assertEqual(sp_params.val_size, val_size)
        self.assertEqual(sp_params.random_state, random_state)


if __name__ == "__main__":
    unittest.main()
