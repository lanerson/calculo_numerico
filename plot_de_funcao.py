import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return np.exp(x - np.sqrt(x))

def h(x):
    return x

def plot_graphs():
    x = np.linspace(0.01,3,1000)
    y_g = g(x)
    y_h = h(x)
    plt.plot(x,y_g,label='$g(x) = e^{(x-\sqrt{x})}')
    plt.plot(x,y_h,label='h(x) = x')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()  

plot_graphs()