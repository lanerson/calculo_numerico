import numpy as np
import matplotlib.pyplot as plt

erro = 0.0001
n = 3


def f(x):
    return x

def _f(x):
    return 1

def nfMet(x0,f,_f):
    x1 = x0 - f(x0)/_f(x0)
    if(abs(x1-x0)<erro or abs(f(x1))<erro): return x1
    return(nfMet(x1))


def plot_graphs():
    x = np.linspace(0.01,10,10000)
    yf = f(x)
    plt.plot(x,yf,label='funcao')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
