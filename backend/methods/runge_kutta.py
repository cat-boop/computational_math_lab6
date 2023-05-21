from methods.util.util import calc_eps_runge


def runge_kutta_differentiation(f, x, y0, step, eps):
    y = [y0]

    for i in range(1, len(x)):
        h = step
        y_cur = calc_y(f, x, y0, h)
        y_next = calc_y(f, x, y0, h / 2)

        while calc_eps_runge(y_cur[i], y_next[i], 4) > eps:
            h /= 2
            y_cur = y_next
            y_next = calc_y(f, x, y0, h / 2)

        y.append(y_next[i])

    return y


def calc_y(f, x, y0, step):
    y = [y0]

    for i in range(1, len(x)):
        k1 = step * f(x[i - 1], y[i - 1])
        k2 = step * f(x[i - 1] + step / 2, y[i - 1] + k1 / 2)
        k3 = step * f(x[i - 1] + step / 2, y[i - 1] + k2 / 2)
        k4 = step * f(x[i - 1] + step, y[i - 1] + k3)
        y.append(y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)

    return y
