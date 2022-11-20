from dataclasses import dataclass

from .dataset_params import DatasetParams
from .features_params import FeatureParams
from .model_params import ModelParams
from .preprocessing_params import PreprocessingParams
from .splitting_params import SplittingParams
from marshmallow_dataclass import class_schema
import yaml


@dataclass()
class TotalPipelineParams:
    dataset_params: DatasetParams
    splitting_params: SplittingParams
    preprocessing_params: PreprocessingParams
    feature_params: FeatureParams
    model_params: ModelParams


TrainingPipelineParamsSchema = class_schema(TotalPipelineParams)


def read_training_pipeline_params(path: str) -> TotalPipelineParams:
    with open(path, "r") as input_stream:
        schema = TrainingPipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
