from typing import List
from dataclasses import dataclass


@dataclass()
class DatasetParams:
    input_file_path: str
    output_paths: List[str]
