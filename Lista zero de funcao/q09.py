from numpy import sin, cos,pi
erro = 0.0001
def f(x):
    return x*cos(x)

def _f(x): 
    return cos(x) - x*sin(x)

def bisec(a = 0,b = pi/2):
    c = (a+b)/2
    if(abs(_f(c))<erro): return c
    if(_f(a)*_f(c)<0): return bisec(a,c)
    elif(_f(b)*_f(c)<0): return bisec(b,c)
    else: return "..."


print(bisec())


