from methods.util.util import calc_eps_runge


def enhanced_eiler_differentiation(f, x, y0, step, eps) -> list:
    y = [y0]

    for i in range(1, len(x)):
        h = step
        y_cur = calc_y(f, x, y0, h)
        y_next = calc_y(f, x, y0, h / 2)

        while calc_eps_runge(y_cur[i], y_next[i], 2) > eps:
            h /= 2
            y_cur = y_next
            y_next = calc_y(f, x, y0, h / 2)

        y.append(y_next[i])

    return y


def calc_y(f, x, y0, step):
    y = [y0]

    for i in range(1, len(x)):
        y.append(y[i - 1] + (step / 2) * (f(x[i - 1], y[i - 1]) + f(x[i], y[i - 1] + step * f(x[i - 1], y[i - 1]))))

    return y
