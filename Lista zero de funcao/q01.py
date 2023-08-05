"""

"""
import matplotlib.pylab as plt
import numpy as np

erro = 0.01
n = 3

def f(y):
    return 1-400*(3+y)/(9.81*(3*y+y*y/2)**3)

def f1(y):
    return 9.81*(3*y+y*y/2)**3

def f2(y):
    return 400*(3+y)

def plot_graphs(a,b,c=1000):
    x = np.linspace(a,b,c)
    y_1 = f1(x)
    y_2 = f2(x)
    plt.plot(x,y_1,label='$g(x) = e^{(x-\sqrt{x})}')
    plt.plot(x,y_2,label='h(x) = x')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()  

#plot_graphs(-10,10)
#pelo gráfico, r1 E [-5,-4] e r2 E [1,2] queremos x>0 então exclue-se r1
#achei 1.514

def bisec(a,b,f,k=1):
    c = (a+b)/2
    if(abs(f(c))<erro): 
        print("execução nº {}".format(k))
        return round(c,n)
    if(f(a)*f(c)<0): return bisec(a,c,f,k+1)
    elif(f(b)*f(c)<0): return bisec(c,b,f,k+1)
    else: return "não foi possível encontrar raiz no intervalo"

print(bisec(0.5,2.5,f))
#deu certo na 7º execução x = 1.516

def fPosition(a,b,f,k=1):
    c = (a*abs(f(a))+b*abs(f(b)))/(abs(f(a)+abs(f(b))))
    if(abs(f(c))<erro): 
        print("execução nº {}".format(k))
        return round(c,n)
    if(f(a)*f(c)<0): return bisec(a,c,f,k+1)
    elif(f(b)*f(c)<0): return bisec(c,b,f,k+1)
    else: return "não foi possível encontrar raiz no intervalo"

print(fPosition(0.5,2.5,f))
#deu certo na 9º execução x = 1.516


