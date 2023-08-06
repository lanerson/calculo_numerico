from numpy import sin, cos, pi
erro = 0.0001


def f(x):
    return 9/sin((125+x)*pi/180) + 7/sin((x)*pi/180)


def _f(x):
    return -9*cos((125+x)*pi/180)/(sin((125+x)*pi/180))**2 - 7*cos(x*pi/180)/(sin((x)*pi/180))**2


def bisec(a=0.1, b=54.9):
    c = (a+b)/2
    if (abs(_f(c)) < erro):
        return c
    if (_f(a)*_f(c) < 0):
        return bisec(a, c)
    elif (_f(b)*_f(c) < 0):
        return bisec(c, b)
    else:
        return "oi"


print(bisec())
