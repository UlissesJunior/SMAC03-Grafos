import numpy as np

def insereVertice(matriz):
    for linha in matriz:
        linha.append(0)

    matriz.append([0 for _ in range(len(matriz)+1)])
    
    print(np.array(matriz))

insereVertice([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])