import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2*x**3 - 11.7*x**2 + 17.7*x - 5

# metodo gráfico


def f1(x):
    return 2*x**3 - 11.7*x**2


def f2(x):
    return -17.7*x + 5


def plot_graphs(a, b, c=1000):
    x = np.linspace(a, b, c)
    y1 = f1(x)
    y2 = f2(x)
    plt.plot(x, y1, label='f1(x)')
    plt.plot(x, y2, label='f2(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
# plot_graphs(-10,10)
# achei 3.563 para x E [3,4]


# vou usar isso em todas
n = 3
x0 = 3

# método ponto-fixo


def g1(x):
    return ((11.7/2)*x**2-(17.7/2)*x+2.5)**(1/3)


def pf(x, n):
    while (n > 0):
        x = g1(x)
        n -= 1
    return round(x,4)


print(pf(x0, n))
# 3.1622

# newton-raphson


def _f(x):
    return 6*x**2 - 23.4*x + 17.7


def newton(x, n):
    for i in range(n):
        x = x - f(x)/_f(x)
        # print("execução {}, x = {}".format(i+1,x))
    return round(x, 4)


print(newton(3, n))
# achei 3.7929

# método da secante


def secante(x0, x1, n):
    x2 = (x0*f(x1) - x1*f(x0))/(f(x1)-f(x0))
    if (n > 0):
        return secante(x1, x2, n-1)
    else:
        return round(x2, 4)


print(secante(4, 3, n))
# achei 3.5497
