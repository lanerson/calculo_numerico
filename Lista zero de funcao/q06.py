from numpy import sqrt, linspace
import matplotlib.pylab as plt
erro = 0.000005


def Re(x):
    return 10*(0.1+1/4*sqrt(x))/sqrt(x)


r = 50000  # valor entre 2500 e 1000000
# escolhi a e b de modo que Re(x) satisfaça r
a = 0.000000000001 #Re(a) = 1000002.5
b = 0.000000041     #Re(b) =    4941.1


def f(x):
    return Re(x)-r


def acho_que_e_isso(a, b):
    c = (a+b)/2
    if (abs(f(c)) < erro):
        return c
    if (f(a)*f(c) < 0):
        return acho_que_e_isso(a, c)
    elif (f(b)*f(c) < 0):
        return acho_que_e_isso(c, b)
    else:
        return "vish..."

print(Re(b))
# print(acho_que_e_isso(a, b))
# achei um valor mas não estou confiante
# melhor pedir essa pro professor
