"""Unittest for src.data.make_dataset.read_csv"""

import logging
import unittest
from io import StringIO
import src
from tests import str_generator
from src.data import read_csv


# switch off import-logging
logging.getLogger(src.data.make_dataset.__name__).disabled = True


class TestReadCsv(unittest.TestCase):
    """Tests for read_csv"""
    def test_number_of_rows(self):
        """Should count the number of rows in a CSV file"""
        for row_size in [5, 10, 20]:
            data = StringIO(
                '\n'.join(
                    [','.join(list(str_generator(5))) for _ in
                     range(row_size + 1)])
            )
            dataframe = read_csv(data)
            self.assertEqual(row_size, dataframe.shape[0])

    def test_number_of_columns(self):
        """Should count the number of columns in a CSV file"""
        for column_size in [5, 10, 20]:
            data = StringIO(
                '\n'.join(
                    [','.join(list(str_generator(column_size))) for _ in
                     range(5)])
            )
            dataframe = read_csv(data)
            self.assertEqual(column_size, dataframe.shape[1])


if __name__ == "__main__":
    unittest.main()
