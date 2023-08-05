from numpy import pi
R = 3
n = 10
def f(h):
    return pi*(h**2)*(3*R-h)/3

def _f(h):
    return 2*pi*R*h-pi*h**2
x0 = 10 #não foi dado na questão
x1 = x0
for i in range(n):
    x1 = x1 - (f(x1)-30)/_f(x1)
    print(f"iteração {i+1} x = {round(x1,5)}\n {f(x1)} erro = {(1-abs(f(x1)/30)):.5%}")
