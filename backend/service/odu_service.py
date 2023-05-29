import math
from dao import odu_dao
from dto.odu_response_dto import OduResponseDto
from dto.point import Point
from mapper.odu_to_odu_dto_mapper import map
from methods.enhanced_eiler import enhanced_eiler_differentiation
from methods.miln import miln_differentiation
from methods.runge_kutta import runge_kutta_differentiation


def get_available_odu_dtos():
    odus = odu_dao.get_available_odus()

    return [map(odu) for odu in odus]


def find_best_similar(id, x0, y0, interval_length, step, eps):
    odu = odu_dao.get_odu_by_id(id)

    n = math.ceil(interval_length / step) + 1

    x = [x0 + step * i for i in range(n)]

    y_eiler = enhanced_eiler_differentiation(odu.function, x, y0, step, eps)
    y_runge_kutta = runge_kutta_differentiation(odu.function, x, y0, step, eps)

    try:
        y_miln = miln_differentiation(odu.function, x, y0, step, eps)
    except ValueError:
        y_miln = None

    enhanced_eiler = [Point(x=xi, y=yi) for xi, yi in zip(x, y_eiler)]
    runge_kutta = [Point(x=xi, y=yi) for xi, yi in zip(x, y_runge_kutta)]
    miln = [] if y_miln is None else [Point(x=xi, y=yi) for xi, yi in zip(x, y_miln)]

    x_min, x_max = min(x), max(x)
    y_min = min(min(y_eiler), min(y_runge_kutta), min(y_eiler if y_miln is None else y_miln))
    y_max = max(max(y_eiler), max(y_runge_kutta), max(y_eiler if y_miln is None else y_miln))

    c = odu.function_c(x0, y0)

    perfect_solution = [Point(x=x0, y=y0)]
    for i in range(n - 1):
        perfect_solution.append(Point(x=x[i + 1], y=odu.function_c(x[i + 1], c)))

    return OduResponseDto(enhanced_eiler=enhanced_eiler, runge_kutta=runge_kutta, miln=miln,
                          perfect_solution=perfect_solution, x_range=[x_min, x_max], y_range=[y_min, y_max])
