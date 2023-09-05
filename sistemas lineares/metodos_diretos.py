import numpy as np


# Para matrizes triangulares
# triangular inferior
def SubInf(L, bs):
    n = bs.size
    xs = np.zeros(n)
    for i in range(n):
        xs[i] = (bs[i] - L[i, :i] @ xs[:i]) / L[i, i]
    return xs


# triangular superior
def SubSup(U, bs):
    n = bs.size
    xs = np.zeros(n)
    for i in reversed(range(n)):
        xs[i] = (bs[i] - U[i, i + 1 :] @ xs[i + 1 :]) / U[i, i]
    return xs


L = np.diag([2, 1, 1])
U = np.diag([2, 1, 1])
bs = np.array([2, 2, 2])
print(SubInf(L, bs))
print(SubSup(U, bs))


# tô considerando que a matriz é 
def ElimGauss(matriz,resul):
    A = np.copy(matriz)
    b = np.copy(resul)
    n = b.size
    for j in range(n-1):
        # pivotando
        # k = np.argmax(np.abs(A[j:,j])) + j
        # if k != j:
        #     A[j,:], A[k,:] = A[k,:], A[j,:].copy()
        #     b[j], b[k] = b[k], b[j]
        for i in range(j+1,n):
            m = A[i,j]/A[j,j]
            A[i,j:] -= m* A[j,j:]
            b[i] -= m*b[j]
    return A,b

def dec_LU(matriz):
    U = np.copy(matriz)
    n = len(U) # poderia usar também U.shape[0]
    L = np.identity(n)
    for j in range(n-1):
        # pivotando
        # k = np.argmax(np.abs(U[j:,j])) + j
        # if k != j:
        #     U[j,:], U[k,:] = U[k,:], U[j,:].copy()

        for i in range(j+1,n):
            m = U[i,j] / U[j,j]
            U[i,j:] -= m * U[j,j:]
            L[i,j] += m
    return L,U

# se a matriz A é simétrica, dá converter ela
# em 2, L triangular inferior e D diagonal, tal que
# A = LDL^T
def LDLT(mat):
    A = np.copy(mat)
    n = len(A)
    for j in range(n-1):
        for i in range(j+1,n):
            m = A[i,j]/A[j,j]
            A[i,j+1:] -= m * A[j,j+1:]
            A[i,j] = m
        for i in range(j+1,n):
            A[j,i] = A[i,j]
    return A


def choleski(A):
    L=A.copy()
    n = len(A)
    for k in range(n):
        try:
            L[k,k] = np.sqrt(L[k,k]- L[k,:k]@L[k,:k])
        except ValueError:
            print('matriz não é definita e positiva')
        for i in range(k+1,n):
            L[i,k] = (L[i,k] - L[i,:k]@L[k,:k])/L[k,k]

    for k in range(1,n): L[:k,k] = 0.0
    return L

# tridiagonal
# depois eu tento entender
def Sol_Sist_Trid(c,d,e,b):
  n=len(d)
  k=np.ones((n))
  t=np.ones((n))
  x =np.ones((n))
  for i in range(n):
    dem=d[i] - c[i]*t[i-1]
    k[i] =(b[i] -c[i]*k[i-1])/dem
    t[i]=e[i]/dem
  x[n-1]=k[n-1]
  for i in reversed(range(n-1)):
    x[i]=k[i] - t[i]*x[i+1]
  return x

# pentadiagonal
# T-T
def sol_pentadiagonal(a,c,d,e,f,b):
  n=len(d)
  p=np.zeros((n))
  t=np.zeros((n))
  v= np.zeros((n))
  x =np.zeros((n))
  p[0]=b[0]/d[0]
  t[0]=e[0]/d[0]
  v[0]=f[0]/d[0]
  for i in range(n):
    l=c[i] - a[i]*t[i-2]
    k=d[i] -l*t[i-1] -a[i]*v[i-2]
    p[i] =(b[i] -a[i]*p[i-2] -l*p[i-1])/k
    t[i]=(e[i]-l*v[i-1])/k
    v[i]=f[i]/k
  x[n-1]=p[n-1]
  x[n-2]=p[n-2] - t[n-2]*x[n-1]
  for i in reversed(range(n-2)):
    x[i]=p[i] - t[i]*x[i+1] -v[i]*x[i+2]
  return x
