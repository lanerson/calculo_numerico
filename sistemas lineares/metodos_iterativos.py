import numpy as np

# método de Jacobi
def sol_jacobi(A,b,x0,erro, kmax=100):
  d =np.diag(A)
  for k in range(kmax):
    r = b - A@x0
    h = r/d # como se fosse o x1
    x0 += h
    print(f"{k+1}º = {x0}\n")
    if abs(np.max(np.abs(h))/max(x0)) < erro:
      break
  return x0

# método de Gauss-Seidel
def SubInf(L, bs):
    n = bs.size
    xs = np.zeros(n)
    for i in range(n):
        xs[i] = (bs[i] - L[i, :i] @ xs[:i]) / L[i, i]
    return xs
def sol_gaussseidel(A,b,x0,erro,kmax=100):
  M =np.tril(A)
  for k in range(kmax):
    r = b - A@x0 # tipo o x1
    h = SubInf(M,r) # faz muito sentido fazer isso
    x0 += h
    print(f"{k+1}º = {x0}\n")
    if abs(np.max(np.abs(h))/max(x0)) < erro:
      break
  return x0
# testes
A = np.array([[5.,1,1],[3,4,1],[3,3,6]])
b = np.array([5.,6,0])
x0 = np.array([0.,0,0])
# sol_jacobi(A,b,x0,0.05)
# sol_gaussseidel(A,b,x0,0.05)
# dá bão

# cansei
#   Para NÃO-LINEARES
# Newton-Raphson

# Newton Modificado
