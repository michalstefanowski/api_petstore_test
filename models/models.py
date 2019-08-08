from enum import Enum
from typing import List, Dict, Union

import attr
import jsons
from attr import dataclass


class PetStatus(Enum):
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"


@dataclass
class PetDto:
    id: int
    photo_urls: List[str]
    status: str
    tags: List[Dict[str, Union[int, str]]] = attr.ib(default=None)
    category: Dict[str, Union[int, str]] = attr.ib(default=None)
    name: str = attr.ib(default=None)

    def to_dict(self):
        return jsons.dump(self.__dict__, key_transformer=jsons.KEY_TRANSFORMER_CAMELCASE)
