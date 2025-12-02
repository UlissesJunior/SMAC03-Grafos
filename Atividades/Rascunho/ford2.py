def caminho(residual, origem, destino):
    qtdNos = len(residual)
    pai = [-1] * qtdNos
    pilha = [origem]
    pai[origem] = origem

    while pilha:
        noAtual = pilha.pop()

        if(noAtual == destino): 
            return pai

        for vizinho in range(qtdNos):
            capacidadeDisponivel = residual[noAtual][noVizinho]

            if(capacidadeDisponivel > 0 and pai[vizinho] == -1):
                pai[vizinho] = noAtual
                pilha.append(vizinho)
        
    return None

def FordFulkerson(grafo, origem, destino):
    qtdNos = len(grafo)
    residual = [linha[:] for linha in capacidade]
    fluxo_total = 0 

    while True:
        pai = caminho(grafo, origem, destino)
        if(pai is None):
            break

        gargalo = float('inf')
        noAtual = destino

        while noAtual != origem:
            noAnterior = pai[noAtual]
            gargalo = min(gargalo, residual[noAnterior][noAtual])
            noAtual = noAnterior

        noAtual = destino

        while noAtual != origem>
            noAnterior = pai[noAtual]
            residual[noAnterior][noAtual] -= gargalo
            residual[noAtual][noAnterior] += gargalo
            noAtual = noAnterior

        fluxo_total += gargalo 

        return fluxoTotal