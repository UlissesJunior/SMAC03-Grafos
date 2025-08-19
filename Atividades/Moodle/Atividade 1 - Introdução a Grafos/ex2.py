def valorCelula(matriz, linha, coluna):
    tamanhoMatrizLinha = len(matriz)
    tamanhoMatrizColuna = len(matriz[0])
    
    if linha > tamanhoMatrizLinha or coluna > tamanhoMatrizColuna:
        print('Erro')
    else:
        print(f'Celula[{linha}][{coluna}] =',matriz[linha][coluna])