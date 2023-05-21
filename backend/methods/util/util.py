def calc_eps_runge(y_cur, y_next, p):
    print(abs(y_cur - y_next) / (2 ** p - 1))
    return abs(y_cur - y_next) / (2 ** p - 1)


def calc_eps_solution(solution, x, y):
    c = y[0] - x[0]

    eps = max([abs(solution(xi, c) - yi) for xi, yi in zip(x, y)])

    return eps
