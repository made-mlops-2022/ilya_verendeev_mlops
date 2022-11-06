from typing import List
from dataclasses import dataclass


@dataclass()
class FeatureParams:
    categorical_features: List[str]
    numerical_features: List[str]
    target_col: str
