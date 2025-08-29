import numpy as np

def removeVertice(matriz, v):
    for i in range(len(matriz)):
        matriz[i][v] = -1
        matriz[v][i] = -1
        
    print(np.array(matriz))
    
removeVertice([[0, 1,	0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 2)