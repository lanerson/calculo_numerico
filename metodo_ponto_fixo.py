"""
seja f(x) a função em análise, tome f(x) = 0 e ajuste a equação
de modo a obter g(x) = x, pode haver várias formas
g(x) precisa ser escolhida de modo que:
- g(x) e g'(x) sejam contínuas no intervalo
- |g'(x)| < M < 1 em todo o intervalo
"""
import numpy as np
import matplotlib.pyplot as plt

erro = 0.0001
n = 3


def f(x):
    return x-1


def g(x):
    return 1  # aqui vc coloca a função g conveniente


"""
só se quiser
def _g(x):
    return 1 #aqui vc coloca a derivada de g
"""

# método do ponto fixo


def mpf(x0, f):
    x1 = g(x0)
    if (abs(x1-x0) < erro or abs(f(x1)) < erro):
        return round(x1, n)
    return mpf(x1, f)
