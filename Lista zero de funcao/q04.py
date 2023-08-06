import matplotlib.pyplot as plt
import numpy as np
k1 = 50000
k2 = 40
m = 90
g = 9.81
h = 0.45
erro = 0.0001
n = 4


def plot_graph(a, b, f):
    x = np.linspace(a, b, 1000)
    y = f(x)
    plt.plot(x, y)
    plt.show()


def f(d):
    return 2*k2*d**(5/2)/5+0.5*k1*d**2 - m*g*d - m*g*h


def _f(d):
    return 5*k2*d**(3/2)/5 + k1*d - m*g


def newton(x0, f, _f):
    x1 = x0 - f(x0)/_f(x0)
    if (abs(x1-x0) < erro or abs(f(x1)) < erro):
        return round(x1, n)
    else:
        return newton(x1, f, _f)


# só pra ver mais ou menos onde a função zera
# plot_graph(0,5,f)
# print(f(1))
# print(newton(0.1, f, _f))
# achei 0.1449
