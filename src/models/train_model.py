"""train model and save it"""

import pickle
import logging
from typing import Union
from pathlib import Path, PurePath
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from src.entities.model_params import ModelParams

SklearnClassificationModel = Union[RandomForestClassifier, LogisticRegression]

logging.basicConfig(
    filename=PurePath(Path(__file__).parents[1], Path(f"logs/logs.log")),
    format="%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.DEBUG,
    filemode="w",
)
logger = logging.getLogger(__name__)


def train_model(
    features: pd.DataFrame, target: pd.Series, model_params: ModelParams
) -> SklearnClassificationModel:
    """train model function. Need to choose model type"""
    logger.debug("In function src.models.train_model.train_model")
    if model_params.model_name == "RandomForestClassifier":
        logger.info("Was used RandomForestClassifier")
        model = RandomForestClassifier()
        param_key = {}
        for key, value in zip(model._get_param_names(), model_params.parameters):
            param_key[key] = value
        model.set_params(**param_key)
    elif model_params.model_name == "LogisticRegression":
        logger.info("Was used LogisticRegression")
        model = LogisticRegression()
    else:
        raise ValueError("Not known model type")
    model.fit(features, target)
    logger.info("Model training done")
    logger.debug("Out of function src.models.train_model.train_model")
    return model


def save_model(model: SklearnClassificationModel, model_params: ModelParams) -> None:
    """save model to file"""
    logger.debug("In function src.models.train_model.save_model")
    with open(model_params.model_save_path, "wb") as file:
        pickle.dump(model, file)
    logger.info("Model was saved in path: %s", model_params.model_save_path)
    logger.debug("Out of function src.models.train_model.save_model")
