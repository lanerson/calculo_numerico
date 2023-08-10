from numpy import pi, linspace
import matplotlib.pyplot as plt
erro = 0.001
n = 4
a = 0.9
q1 = 2*10**(-5)
q2 = q1
e0 = 8.85*10**(-12)
k = q1*q2/(4*pi*e0)
F = 1.25


def f(x):
    return k*x/(x**2+a**2)**(3/2)-F


def grafico():
    x = linspace(-10, 10, 1000)
    y = f(x)
    plt.plot(x, y)
    plt.grid(True)
    plt.show()


def g1(x):
    return F*(x**2+a**2)**(3/2)/k


def g2(x):
    return ((k*x / F)**(2/3) - a**2)**(1/2)


def ponto_fixo(x, g):
    x1 = g(x)
    if (abs(x1-x) < erro or abs(f(x1)) < erro):
        return round(x1, n)
    else:
        return ponto_fixo(x1, g)


grafico()
print(ponto_fixo(1, g1))
print(ponto_fixo(1, g2))

# 0.2951
