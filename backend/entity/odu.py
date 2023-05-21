from typing import Callable


class Odu:
    id: int
    function: Callable[[float, float], float]
    solution: Callable[[float, float], float]
    string_representation: str

    def __init__(self, id: int, function: Callable[[float, float], float], solution: Callable[[float, float], float],
                 string_representation: str):
        self.id = id
        self.function = function
        self.solution = solution
        self.string_representation = string_representation
