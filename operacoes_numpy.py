import numpy as np
# geralmente vc define um array numpy assim
A = np.array([[1,2,3,],[1,2,3],[1,2,3]])

# matrizes rápidas
I = np.identity(3) # autoexplicativo
ones = np.ones((3,4)) # cria uma matriz de uns de tamanho 3 por 4 
zeros = np.zeros((5,5)) # cria uma matriz de zeros de tamanho 5 por 5
B = np.arange(10) # cria um array a partir da função range(comeco, fim, passo)
B = B.reshape((2,5)) # retorna a transformação da matriz 1 por 10 em uma 2 por 5
olho = np.eye(3,5,k=2) # matriz identidade bugada, preenchida na diagonal k+1
diag = np.diag([1,2,3,4]) # matriz diagonal, achei util

def f(m,n): return m+n
F1 = np.fromfunction(f,(4,5)) # m,n são os indices dos elementos da matriz 4 por 5
F2 = np.fromfunction(lambda m,n: m+n,(4,5)) # equivalente usando função anônima
F3 = np.array([i+j for i in range(3) for j in range(4)]).reshape(3,4)
    # esse é mais rápido computacionalmente

"""
            SLICING

a gente separa as linhas e colunas de uma matriz pela linha
depois disso, é aquela mesma parada de uma lista comum
lista[começo:fim:passo]~
se vc não escrever nada ele pega o padrão: começo é zero, fim é -1, e passo é 1
obs: passo pode ser omitido
lista[começo:fim]
"""


# Operações com matrizes

soma = np.array([x + y for x in range(1,5) for y in range(1,5)]).reshape(4,4)
dif = np.array([x - y for x in range(1,5) for y in range(1,5)]).reshape(4,4)

t1 = soma - dif
t2 = soma + dif
t3 = soma * dif # produto termo a termo
t4 = soma @ dif # produto matricial, só funciona com arrays numpy
t5 = soma / dif # divisão termo a termo
a,b = 10,11
t6 = a*soma + b*dif # combinação linear das matrizes, normal
somaT = soma.T # matriz transposta
detSoma = np.linalg.det(soma) # determinante da matriz
invSoma = np.linalg.inv(soma) # matriz inversa da soma






