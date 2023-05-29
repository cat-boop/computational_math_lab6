import math
from typing import List

from entity.odu import Odu

odu_storage = {
    1: Odu(1,
           lambda x, y: x + y,
           lambda x, y: math.exp(-x) * (x + y + 1),
           lambda x, c: c * math.exp(x) - x - 1,
           "x + y"),
    2: Odu(2,
           lambda x, y: x * y,
           lambda x, y: math.exp((-x ** 2) / 2) * y,
           lambda x, c: c * math.exp((x ** 2) / 2),
           "x * y"),
    3: Odu(3,
           lambda x, y: x + y * x,
           lambda x, y: math.exp((-x ** 2) / 2) * (y + 1),
           lambda x, c: c * math.exp((x ** 2) / 2) - 1,
           "x + y * x"),
    4: Odu(4,
           lambda x, y: y + (1 + x) * (y ** 2),
           lambda x, y: -math.exp(x) * (x * y + 1) / y,
           lambda x, c: -math.exp(x) / (c + math.exp(x) * x),
           "y + (1 + x) * y ^ 2")
}


def get_available_odus() -> List[Odu]:
    return odu_storage.values()


def get_odu_by_id(id: int) -> Odu | None:
    if id not in odu_storage.keys():
        return None
    return odu_storage[id]
