def removeAresta(matriz, linha, coluna):   
     matriz[linha][coluna] = 0
     matriz[coluna][linha] = 0
     print(matriz)