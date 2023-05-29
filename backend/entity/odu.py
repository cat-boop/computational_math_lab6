from typing import Callable


class Odu:
    id: int
    function: Callable[[float, float], float]
    function_c: Callable[[float, float], float]
    solution: Callable[[float, float], float]
    string_representation: str

    def __init__(self, id: int, function: Callable[[float, float], float], function_c: Callable[[float, float], float],
                 solution: Callable[[float, float], float], string_representation: str):
        self.id = id
        self.function = function
        self.function_c = function_c
        self.solution = solution
        self.string_representation = string_representation
