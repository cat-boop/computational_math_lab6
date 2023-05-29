from typing import List

from pydantic import BaseModel

from dto.point import Point


class OduResponseDto(BaseModel):
    enhanced_eiler: List[Point]
    runge_kutta: List[Point]
    miln: List[Point]
    perfect_solution: List[Point]
    x_range: List[float]
    y_range: List[float]
