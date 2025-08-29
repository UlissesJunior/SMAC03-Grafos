def insereAresta(matriz, linha, coluna):   
     matriz[linha][coluna] +=1
     matriz[coluna][linha] +=1
     print(matriz)