import pickle
import logging
from typing import Dict, Union
from pathlib import Path, PurePath
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from src.entities import ModelParams

SklearnClassificationModel = Union[RandomForestClassifier, LogisticRegression]

logging.basicConfig(
    filename=PurePath(Path(__file__).parents[1], Path(f"logs/logs.log")),
    format="%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.DEBUG,
    filemode="w",
)
logger = logging.getLogger(__name__)


def predict_model(
    model: SklearnClassificationModel, features: pd.DataFrame
) -> np.ndarray:
    logger.debug("In function src.models.predict_model.predict_model")
    predicts = model.predict(features)
    logger.info("Model predict target for %s", model.__str__)
    logger.debug("Out of function src.models.predict_model.predict_model")
    return predicts


def evaluate_model(predicts: np.ndarray, target: pd.Series) -> Dict[str, float]:
    logger.debug("In function src.models.predict_model.evaluate_model")
    accuracy_metrics = accuracy_score(target, predicts)
    f1_metrics = f1_score(target, predicts)
    logger.info("Get metrics: accuracy=%s, f1=%s", accuracy_metrics, f1_metrics)
    logger.debug("Out of function src.models.predict_model.evaluate_model")
    return {
        "accuracy": accuracy_metrics,
        "f1": f1_metrics,
    }


def load_model(model_params: ModelParams) -> SklearnClassificationModel:
    logger.debug("In function src.models.predict_model.load_model")
    with open(model_params.model_save_path, "rb") as file:
        loaded_model = pickle.load(file)
    logger.info("Model loaded from %s", model_params.model_save_path)
    logger.debug("In function src.models.predict_model.load_model")
    return loaded_model
