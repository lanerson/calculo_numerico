from math import exp, sqrt


def g(x):
    return exp(x - sqrt(x))


def fixedpoint(g, xold, kmax=10, tol=1.e-8):
    for k in range(1, kmax):
        xnew = g(xold)  # x_{k+1} = g(x_{k})
        xdiff = xnew - xold
        print("{0:2d} {1:1.16f} {2:1.16f}".format(k, xnew, xdiff))
        if abs(xdiff/xnew) < tol:
            break
        xold = xnew
    else:
        xnew = None
    return xnew


fixedpoint(g, 4)
