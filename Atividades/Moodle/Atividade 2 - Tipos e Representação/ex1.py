import numpy as np

def verificaAdjacencia(matrizAdjacencia, verticeI, verticeJ):
    matriz = np.array(matrizAdjacencia)
    if matriz[verticeI][verticeJ] != 0:
        return True
    return False
