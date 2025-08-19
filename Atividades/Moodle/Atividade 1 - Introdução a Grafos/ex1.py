def dimensaoMatriz(matriz):
    valoresDiagonal = []
    tamanhoMatrizLinha = len(matriz)
    tamanhoMatrizColuna = len(matriz[0])
    for i in range(min(tamanhoMatrizLinha, tamanhoMatrizColuna)):
        valoresDiagonal.append(matriz[i][i])
    
    valoresDiagonal = ' '.join(map(str, valoresDiagonal))
    
    print(f'({tamanhoMatrizLinha}, {tamanhoMatrizColuna})', f'[{valoresDiagonal}]')