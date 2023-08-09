from numpy import pi
R = 3
n = 3


def f(h):
    return 30 - pi*(h**2)*(3*R-h)/3


def _f(h):
    return -2*pi*R*h-pi*h**2


x0 = 1  # não foi dado na questão
x1 = x0
x_base = 2.026905728309901  # descobre usando o método que preferir


def newton(x0, n, k=1):
    x1 = x0 - f(x0)/_f(x0)
    print(f"iteração {k}, x = {round(x1,4)} erro = {abs(1-x1/x_base):.2%}")
    while k < n:
        return newton(x1, n, k+1)
    return x1


newton(x0, 3)

# print(f(x_base))
