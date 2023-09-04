import numpy as np
n = 3
tr = np.array([x+y for x in range(n) for y in range(n)]).reshape(3,3)
bs = np.array([5,5,5])

# para matriz triangular inferior
def SubSuc(A,b):
    n = b.size
    x = np.zeros(n)
    for i in range(n):
        x[i] = (b[i] - A[i,:i]@x[:i]) / A[i,i]
    return x

# para matriz triangular superior
def SubRet(A,b):
    n = b.size
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (b[i] - A[i,i+1:]@x[i+1:]) / A[i,i]
    return x
# aquele que a gente já conhece com o pivotamento parcial
def ElimGauss(mat,resul):
    A = np.copy(mat)
    b = np.copy(resul)
    n = b.size
    for j in range(n-1):
        #Se eu tiver que pivotar parcialmente
        k = np.argmax(np.abs(A[j:,j])) + j
        if k != j:
            A[k,:], A[j,:] = A[j,:], A[k,:].copy()
            b[j], b[k] = b[k], b[j]
        for i in range(j+1, n):
            m = A[i,j]/ A[j,j]
            A[i,j:] -= m * A[j,j:]
            b[i] -= m * b[j]

""" L é uma matriz triangular inferior e U é triangular superior
é só lembrar daquelas paradas de algebra linear de operações elementares:
    combinação linear, troca de linha e multiplicação por escalar
"""
def dec_LU(mat):
    U = np.copy(mat)
    n = len(U)
    L = np.identity(n)
    for j in range(n-1):
        for i in range(j+1,n):
            m = U[i,j] / U[j,j]
            U[i,j:] -= m * U[j,j:]
            L[i,j] += m
    return L,U
    
"""
Aqui ela vai retornar na forma reduzida
abaixo da diagonal principal vai ter L, na diagonal principal
vai ter D e acima, L, que no caso é L transposta
a diagonal principal de L é preenchida com 1
"""
def LDLT(A):
    x = np.copy(A)
    n = len(x)
    for j in range(n-1):
        m = 0
        for i in range(j+1,n):
            m = x[i,j]/ x[j,j]
            x[i,j+1:] -= m * x[j,j+1:]
            x[i,j] = m
        for i in range(j+1,n):
            x[j,i] = x[i,j]
    return x

"""
supondo que a matriz A é simetrica e 
positiva definida, ou seja, que, dado x no Rn
x.T * A * x > 0
nesse caso, a matriz pode ser escrita como A = L * L.T (L transposta)
"""
def cholesky(A):
    L = np.copy(A)
    for k in range(n):
        try: # essa estrutura é só pra apontar o erro caso a matriz de entrada não seja positiva definida
            L[k,k] = np.sqrt(A[k,k]@A[k,k]-L[k,:k]@L[j,:j]) 
        except:
            print("essa matriz não é positiva definida")
        for i in range(k+1,n+1):
            L[i,k] = (A[i,k]-L[i,:k]@L[k,:k]) / L[k,k]
    for k in range(n-1): L[k:k+1:] = 0.0 
    return L

