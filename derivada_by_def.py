from numpy import sin, cos, linspace, pi
import matplotlib.pyplot as plt


def f(x):
    return sin(x)
# se vc quiser o valor
def _f(x, dx = 0.000000001):
    return (f(x+dx) - f(x))/dx
# se vc quiser a função
def df(f, dx=0.000000001):
    def _f(x):
        return (f(x+dx) - f(x))/dx
    return _f
y_linha = df(f)


print(f(pi/3))
# 0.8660254037844386
print(df(pi/3))
# 0.5000000413701855
# parece funcional
