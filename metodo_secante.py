erro = 0.001
n = 3

def f(x):
    return x-1

def sec(x0,x1,f):
    x2 = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
    if (abs(f(x2))<erro): return round(x2,n)
    if (abs(f(x2))>abs(f(x1))): return "não tá convergindo"
    return sec(x1,x2,f)



    
        