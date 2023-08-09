import matplotlib.pyplot as plt
import numpy as np
import pandas
e = 0.9
erro = 0.0001


def f(y):
    return y - e*np.sin(y)


def _f(y):
    return 1 - e*np.cos(y)


def newton(x0, y0=1):
    y1 = y0 - (f(y0)-x0)/_f(y0)
    if (abs(f(y1)-x0) < erro):
        return y1
    else:
        return newton(x0, y1)


lista = []
for i in range(30):
    lista.append(np.pi*(i+1)/30)

_lista = []

for num in lista:
    _lista.append(newton(num))

df = pandas.DataFrame(lista, _lista)
print(df)
