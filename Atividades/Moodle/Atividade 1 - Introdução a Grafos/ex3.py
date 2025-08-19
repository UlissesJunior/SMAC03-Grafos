def criaDicionario(matriz):
    dic = {}
    tamanhoMatrizLinha = len(matriz)
    tamanhoMatrizColuna = len(matriz[0])

    for i in range(tamanhoMatrizLinha):
        lista = []
        for j in range(tamanhoMatrizColuna):
            if matriz[i][j] > 0:
                lista.extend([j] * matriz[i][j])
        dic[i] = lista
    return dic
