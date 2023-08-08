import math
import numpy as np

R = 3

# declaração da função dada


def f(h):
    return 30 - math.pi*h**2*(3*R-h)/3

# derivada de f


def dfdh(h):
    return -math.pi*h*(2*R-h)


# chute inicial
initialGuess = 2

# tolerância e máximas iterações
tol = 0.01
maxIter = 3

# método de Newton-Raphson


def newtonRaphson(f, dfdh, h0, tol, maxIter):

    i = 0
    h_k = [h0]
    y_k = [f(h0)]
    
    while (abs(f(h_k[-1])) > tol or i < maxIter):
        print("está rodando")
        next_h = h_k[-1] - f(h_k[-1])/dfdh(h_k[-1])

        h_k.append(next_h)
        y_k.append(f(next_h))
        i+=1
    erroRel = (next_h - h_k[-1])/h_k[-1]

    print('O erro relativo da {}-ésima iteração é {}'.format(i+1, erroRel))

    # print(h_k);
    # print(y_k);

    return h_k[-1]


root = newtonRaphson(f, dfdh, initialGuess, tol, maxIter)

print('Método de Newton-Raphson: a raiz vale ' + str(root))
