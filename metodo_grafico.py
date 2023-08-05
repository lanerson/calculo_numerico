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


def plot_graphs(a,b,c=1000):
    x = np.linspace(a,b,c)
    y1 = f1(x)
    y2 = f2(x)
    plt.plot(x,y1,label='f1(x) = x³')
    plt.plot(x,y2,label='f2(x) = 9x-3')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show() 

plot_graphs(-4,3)

"""
Analisando o gráfico vemos que há raízes nos intervalos [-4,-3],[0,1] e[2,3]
"""