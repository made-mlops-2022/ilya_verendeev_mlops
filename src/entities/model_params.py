from dataclasses import dataclass, field


@dataclass()
class ModelParams:
    model_save_path: str
    model_name: str
    parameters: list
