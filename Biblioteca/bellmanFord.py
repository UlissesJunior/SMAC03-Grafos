def encontrar_caminho_aumentante(grafo_residual, origem, destino):
    pai = {origem: None}
    pilha = [origem]

    while pilha:
        no_atual = pilha.pop()
        if no_atual == destino:
            return pai

        for vizinho in grafo_residual[no_atual]:
            capacidade_restante = grafo_residual[no_atual][vizinho]
            if capacidade_restante > 0 and vizinho not in pai:
                pai[vizinho] = no_atual
                pilha.append(vizinho)

    return None

def ford_fulkerson(grafo_capacidade, origem, destino):
    grafo_residual = {no: grafo_capacidade[no].copy() for no in grafo_capacidade}
    fluxo_total = 0

    while True:
        caminho_pai = encontrar_caminho_aumentante(grafo_residual, origem, destino)
        if caminho_pai is None:
            break

        gargalo = float('inf')
        no_atual = destino
        while caminho_pai[no_atual] is not None:
            no_anterior = caminho_pai[no_atual]
            gargalo = min(gargalo, grafo_residual[no_anterior][no_atual])
            no_atual = no_anterior

        no_atual = destino
        while caminho_pai[no_atual] is not None:
            no_anterior = caminho_pai[no_atual]
            grafo_residual[no_anterior][no_atual] -= gargalo
            grafo_residual[no_atual][no_anterior] += gargalo
            no_atual = no_anterior

        fluxo_total += gargalo

    return fluxo_total
