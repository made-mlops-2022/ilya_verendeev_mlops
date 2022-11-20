"""Unittest for src.model_pipeline"""

import logging
import unittest
from click.testing import CliRunner
from src.model_pipeline import model_pipe
import src


# switch off import-logging
logging.getLogger(src.model_pipeline.__name__).disabled = True


class TestPipeline(unittest.TestCase):
    """Tests for main pipeline"""
    def test_click(self):
        """Should test click"""
        runner = CliRunner()
        result = runner.invoke(model_pipe,
                               ['--process-type=train', 'configs/logistic_regression_config.yaml'])
        assert result.exit_code == 0


if __name__ == "__main__":
    unittest.main()
