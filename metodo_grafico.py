"""
Consiste em reparar a função em duas partes e comparar os dois gráficos gerados
vou usar como exemplo a função f(x) = x³-9x+3
queremos f(x)=0 então x³-9x+3 - 0
x³ = 9x-3
f1(x) = x³ e f2(x) = 9x-3
"""

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**3-9*x+3


def f1(x):
    return x**3


def f2(x):
    return 9*x-3


def grafico(a, b, c=1000):
    x = np.linspace(a, b, c)
    y = f(x)
    raizes = []
    raiz = 0
    for i in range(len(x)-1):
        if (y[i]*y[i+1] < 0):
            raiz = (x[i]*abs(f(x[i+1])) + x[i+1]*abs(f(x[i]))) / \
                (abs(f(x[i+1])) + abs(f(x[i])))
            raizes.append(round(raiz, 3))
        elif (y[i] == 0):
            raiz = x[i]
            raizes.append(round(raiz, 3))
    print(raizes)


grafico(-10, 10)

"""
Analisando o gráfico vemos que há raízes nos intervalos [-4,-3],[0,1] e[2,3]
"""
