from numpy import sin, cos, linspace, pi
import matplotlib.pyplot as plt


def f(x):
    return sin(x)


def df(x, dx=0.000000001):
    return (f(x+dx)-f(x))/dx


print(f(pi/3))
# 0.8660254037844386
print(df(pi/3))
# 0.5000000413701855
# parece funcional
