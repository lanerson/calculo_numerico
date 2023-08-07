import matplotlib.pyplot as plt
import numpy as np

erro = 0.01
n = 3


def f(y):
    return 1 - 400 * (3 + y) / (9.81 * (3 * y + y * y / 2) ** 3)


def g(y):
    return 0


def plot_graphs():
    y = np.linspace(0.5, 3, 1000)  # Intervalo de y de 0.5 a 3 com 1000 pontos
    y_y = f(y)
    # y_0 = g(y)
    # plt.plot(y, y_0, label='g(y)')
    plt.plot(y, y_y, label='f(y)')  # Adiciona o gráfico de f(y)
    plt.xlabel('y')
    plt.ylabel('f(y)')
    plt.legend()
    plt.grid(True)
    plt.title('Gráfico de f(y)')
    plt.show()


plot_graphs()

# else return;
