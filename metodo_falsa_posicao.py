import numpy as np
import matplotlib.pyplot as plt

erro = 0.0001
n = 3


def f(x):
    return x-1


def falsePosition(a, b, f):
    if (f(a)*f(b) < 0):
        c = (a*abs(f(a))+b*abs(f(b)))/(abs(f(a)+abs(f(b))))
        if (abs(f(c)) < erro):
            return round(c, n)
        if (f(a)*f(c) < 0):
            return falsePosition(a, c, f)
        elif (f(b)*f(c) < 0):
            return falsePosition(c, b, f)
    else:
        return "não foi possível encontrar a raiz ;-;"

# feito pelo Romero
def regulaFalsi(f, x1, x2, maxIter=30, tol=1.0e-9):
    f1 = f(x1)
    if f1 == 0:
        return x1

    f2 = f(x2)
    if f2 == 0:
        return x2

    if np.sign(f1) == np.sign(f2):
        raise ValueError("The roots aren't brackted!")

    x3old = x2
    for i in range(maxIter):
        x3 = (x1 * f2 - x2 * f1) / (f2 - f1)
        ea = abs((x3old - x3) / x3)

        if ea < tol:
            break

        f3 = f(x3)
        if np.sign(f3) != np.sign(f2):
            x1 = x3
            f1 = f3
        else:
            x2 = x3
            f2 = f3

        x3old = x3

    return x3, ea
