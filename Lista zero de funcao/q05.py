from numpy import pi
erro = 0.001
n = 4
a = 0.9
q1 = 2*10**(-5)
q2 = q1
e0 = 8.85*10**(-12)
k = q1*q2/(4*pi*e0)
F = 1.25


def f(x):
    return k*x/(x**2+a**2)**(3/2)


def g(x):
    return F*(x**2+a**2)**(3/2)/k


# Nem vou testar, a questão implora por ponto fixo
def ponto_fixo(x):
    x1 = g(x)
    if (abs(x1-x) < erro or abs(f(x1)) < erro):
        return round(x1, n)
    else:
        return ponto_fixo(x1)


# print(ponto_fixo(0))
# 0.2951
