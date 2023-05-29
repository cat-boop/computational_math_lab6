from methods.runge_kutta import runge_kutta_differentiation


def miln_differentiation(f, x, y0, step, eps):
    if len(x) < 4:
        raise ValueError("For Milan differentiation num of intervals has to be at least 4!")

    runge_result = runge_kutta_differentiation(f, x, y0, step, eps)
    y = runge_result[:4]

    for i in range(4, len(x)):
        y_prediction = prediction(step, f, x, y, i)
        y_correction = correction(step, f, x, y, i, y_prediction)

        while abs(y_correction - y_prediction) > eps:
            y_prediction = y_correction
            y_correction = correction(step, f, x, y, i, y_prediction)
            # print(y_correction)

        y.append(y_correction)

    return y


def prediction(h, f, x, y, i):
    tmp = 2 * f(x[i - 3], y[i - 3]) - f(x[i - 2], y[i - 2]) + 2 * f(x[i - 1], y[i - 1])
    return y[i - 4] + 4 * h * tmp / 3


def correction(h, f, x, y, i, y_pred):
    tmp = f(x[i - 2], y[i - 2]) + 4 * f(x[i - 1], y[i - 1]) + f(x[i], y_pred)
    return y[i - 2] + h * tmp / 3
