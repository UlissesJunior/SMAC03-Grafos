import numpy as np

def calcDensidade(matriz):
    matriz = np.array(matriz)
    qtdVertices = len(matriz)
    sumMatriz = np.sum(matriz)
    densidade = 0    
    if(verificaDigrafo(matriz)):
        densidade = sumMatriz / (qtdVertices * (qtdVertices - 1))
    else:
        numArestas = sumMatriz / 2
        densidade = numArestas / (qtdVertices * (qtdVertices - 1) / 2)
    print(densidade.round(3))
    
def verificaDigrafo(matriz):
    qtdVertices = len(matriz)
    for i in range(qtdVertices):
        for j in range(i + 1, qtdVertices):
            if matriz[i][j] != matriz [j][i]:
                return True
    return False