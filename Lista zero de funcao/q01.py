
import matplotlib.pylab as plt
import numpy as np

erro = 0.01
n = 3


def f(y):
    return 1-400*(3+y)/(9.81*(3*y+y*y/2)**3)


def f1(y):
    return 9.81*(3*y+y*y/2)**3


def f2(y):
    return 400*(3+y)


# método carteado que ele diz ser "método gráfico"
"""
def grafico(a, b, c=1000):
    x = np.linspace(a, b, c)
    y = f(x) 
    raizes = []
    raiz = 0
    for i in range(len(x)-1):
        if (y[i]*y[i+1] < 0):
            raiz = (x[i]*abs(f(x[i+1])) + x[i+1]*abs(f(x[i]))) /
                (abs(f(x[i+1])) + abs(f(x[i])))
            raizes.append(round(raiz, 3))
        elif (y[i] == 0):
            raiz = x[i]
            raizes.append(round(raiz, 3))
    print(raizes)


grafico(-10, 10)
"""


def metodo_grafico(a, b, c=1000):
    x = np.linspace(a, b, c)
    y_1 = f1(x)
    y_2 = f2(x)
    plt.plot(x, y_1, label="f1(x)")
    plt.plot(x, y_2, label="f2(x)")
    plt.grid(True)
    plt.show()


# metodo_grafico(-5, 2)

# -4.255 e 1.514

def bisec(a, b, f, k=1):
    c = (a+b)/2
    if (abs(f(c)) < erro):
        print("execução nº {}".format(k))
        return round(c, n)
    if (f(a)*f(c) < 0):
        return bisec(a, c, f, k+1)
    elif (f(b)*f(c) < 0):
        return bisec(c, b, f, k+1)
    else:
        return "não foi possível encontrar raiz no intervalo"


# print(bisec(0.5, 2.5, f))
# deu certo na 7º execução x = 1.516


def fPosition(a, b, f, k=1):
    c = (a*abs(f(b))+b*abs(f(a)))/(abs(f(a))+abs(f(b)))
    if (abs(f(c)) < erro or k == 10):
        print("execução nº {}, x = {}".format(k, c))
        return round(c, n)
    if (f(a)*f(c) < 0):
        return fPosition(a, c, f, k+1)
    elif (f(b)*f(c) < 0):
        return fPosition(c, b, f, k+1)
    else:
        return "não foi possível encontrar raiz no intervalo"


# print(fPosition(0.5, 2.5, f))
# foi até a 10º achando 2.091
