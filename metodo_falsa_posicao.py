import numpy as np
import matplotlib.pyplot as plt

erro = 0.0001
n = 3

def f(x):
    return x-1

def falsePosition (a,b,f):
    if(f(a)*f(b)<0):
        c = (a*abs(f(a))+b*abs(f(b)))/(abs(f(a)+abs(f(b))))
        if(abs(f(c)) < erro): return round(c,n)
        if(f(a)*f(c)<0):
            return falsePosition(a,c,f)
        elif(f(b)*f(c)<0):
            return falsePosition(c,b,f)  
    else: return "não foi possível encontrar a raiz ;-;" 
