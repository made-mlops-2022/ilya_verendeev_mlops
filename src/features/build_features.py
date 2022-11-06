"""feature preprocessing and target extraction script"""

import logging
from pathlib import Path, PurePath
from typing import Tuple
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures, StandardScaler, KBinsDiscretizer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.entities import FeatureParams, PreprocessingParams

logging.basicConfig(
    filename=PurePath(Path(__file__).parents[1], Path(f"logs/logs.log")),
    format="%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.DEBUG,
    filemode="w",
)
logger = logging.getLogger(__name__)


class PreprocessingTransformer:
    def __init__(
        self, preprocess_params: PreprocessingParams, feature_params: FeatureParams
    ):
        """Prepare data:
        After EDA we know, that we haven't got null-values
        and all categorical columns have numerical representation
        So, one variant of action is numeric preprocessing"""
        self.preprocess_params = preprocess_params
        self.feature_params = feature_params

        pipeline_lvl = []
        if "normalization" in preprocess_params.pipeline:
            pipeline_lvl.append(("normalization", StandardScaler()))
        if "polynomial" in preprocess_params.pipeline:
            pipeline_lvl.append(("polynomial", PolynomialFeatures()))
        if "k-bins" in preprocess_params.pipeline:
            pipeline_lvl.append(("k-bins", KBinsDiscretizer()))
        pipe = Pipeline(pipeline_lvl)

        self.transformer = ColumnTransformer(
            [
                (
                    "total_features",
                    pipe,
                    self.feature_params.numerical_features
                    + self.feature_params.categorical_features,
                )
            ]
        )
        logger.info(
            "Preprocessing transformer consists of [%s]",
            ", ".join([i[0] for i in pipeline_lvl]),
        )

    def transform(self, data):
        return self.transformer.transform(data)

    def fit(self, data):
        self.transformer.fit(data)

    def fit_transform(self, data):
        self.transformer.fit(data)
        return self.transformer.transform(data)

    def get_params(self):
        return self.transformer.get_params()


def extract_target(
    dataframe: pd.DataFrame, feature_params: FeatureParams
) -> Tuple[pd.DataFrame, pd.Series]:
    """Extract target column from dataset
    Return dataframe with variables and series with target"""
    logger.debug("In function src.features.build_features.extract_target")
    target = dataframe[feature_params.target_col]
    data = dataframe.drop(columns=feature_params.target_col)
    logger.info("pd.Series with column = %s", target.name)
    logger.info("pd.DataFrame with columns = %s", data.columns)
    logger.debug("Out of function src.features.build_features.extract_target")
    return data, target
