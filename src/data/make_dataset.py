"""Script for read dataset file and split it to train/val"""

import logging
from typing import Tuple
from pathlib import Path, PurePath
import pandas as pd
from sklearn.model_selection import train_test_split
from src.entities import SplittingParams, DatasetParams

logging.basicConfig(
    filename=PurePath(Path(__file__).parents[1], Path(f'logs/logs.log')),
    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG,
    filemode='w')
logger = logging.getLogger(__name__)


def read_csv(file_path: str) -> pd.DataFrame:
    """Read csv-file with pandas"""
    logger.debug("In function src.data.make_dataset.read_csv")
    raw_df = pd.read_csv(file_path)
    logger.info("Csv file was read, size %s", raw_df.shape[0])
    logger.debug("Out of function src.data.make_dataset.read_csv")
    return raw_df


def split_train_val_data(
        data: pd.DataFrame, split_params: SplittingParams, dataset_params: DatasetParams
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Split data with given params of val_size/random_state
    """
    logger.debug("In function src.data.make_dataset.split_train_val_data")
    train_data, val_data = train_test_split(
        data, test_size=split_params.val_size, random_state=split_params.random_state
    )
    logger.info(
        "Data was processed to train, size = %s, and val, size = %s",
        train_data.shape[0],
        val_data.shape[0],
    )
    train_data.to_csv(dataset_params.output_paths[0])
    val_data.to_csv(dataset_params.output_paths[1])

    return train_data, val_data
