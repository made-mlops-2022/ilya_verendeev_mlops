from dataclasses import dataclass, field
from typing import Union


@dataclass()
class SplittingParams:
    val_size: float = field(default=0.2)
    random_state: Union[int, None] = field(default=None)
