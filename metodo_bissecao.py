"""
1º)Método da bisseção
seja [a,b] com f(a)f(b)<0, então, se a função é contínua,
existe c E [a,b] tal que f(c) = 0
"""

import numpy as np
import matplotlib.pyplot as plt
import time
erro = 0.0001
n = 3

def f(x):
    return x-1

def bisec (a,b,f):
    if(f(a)*f(b)<0):
        c = (a+b)/2
        if(abs(f(c)) < erro): return round(c,3)
        if(f(a)*f(c)<0):
            return bisec(a,c,f)
        elif(f(b)*f(c)<0):
            return bisec(c,b,f)  
    else: return "não foi possível encontrar a raiz ;-;"      
#print(bisec(-1,2,f))

def g(x):
    return x-1




