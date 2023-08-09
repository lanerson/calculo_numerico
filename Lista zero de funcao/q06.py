from numpy import sqrt, linspace, log10 as log
import matplotlib.pylab as plt
erro = 0.000005


def Re(x):
    return 10**(0.1+1/(4*sqrt(x)))/sqrt(x)


r = 50000  # valor entre 2500 e 1000000
# escolhi a e b de modo que Re(x) satisfaça r
a = 0.001  # Re(a) = 1000002.5
b = 0.01  # Re(b) =    4941.1


def f(x):
    return Re(x)-r


def bisec(a, b):
    c = (a+b)/2
    if (abs(f(c)) < erro):
        return c
    if (f(a)*f(c) < 0):
        return bisec(a, c)
    elif (f(b)*f(c) < 0):
        return bisec(c, b)
    else:
        return "vish..."


# print(bisec(a, b))

print(4*log(50000*sqrt(0.0052265))- 0.4-1/(sqrt(0.0052265)))