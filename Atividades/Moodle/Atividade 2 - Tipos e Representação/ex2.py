import numpy as np

def tipoGrafo(matriz):
    matriz = np.array(matriz)
    qtdVertices = len(matriz)

    digrafo = False
    for i in range(qtdVertices):
        for j in range(i + 1, qtdVertices):
            if matriz[i][j] != matriz[j][i]:
                digrafo = True
                break

    temLaco = np.any(np.diag(matriz) > 0)

    temMultiaresta = np.any(matriz > 1)

    if temLaco:
        return print("31") if digrafo else print("30")
    elif temMultiaresta:
        return print("21") if digrafo else print("20")
    else:
        print("1") if digrafo else print("0")