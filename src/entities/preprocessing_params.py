from dataclasses import dataclass
from typing import List


@dataclass()
class PreprocessingParams:
    pipeline: List[str]
