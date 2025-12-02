def encontrar_caminho(residual, origem, destino):
    quantidade_nos = len(residual)
    pai = [-1] * quantidade_nos
    pilha = [origem]
    pai[origem] = origem

    while pilha:
        no_atual = pilha.pop()

        if no_atual == destino:
            return pai

        for vizinho in range(quantidade_nos):
            capacidade_disponivel = residual[no_atual][vizinho]

            if capacidade_disponivel > 0 and pai[vizinho] == -1:
                pai[vizinho] = no_atual
                pilha.append(vizinho)

    return None


def ford_fulkerson(capacidade, origem, destino):
    quantidade_nos = len(capacidade)
    residual = [linha[:] for linha in capacidade]
    fluxo_total = 0

    while True:
        pai = encontrar_caminho(residual, origem, destino)
        if pai is None:
            break

        gargalo = float('inf')
        no_atual = destino

        while no_atual != origem:
            no_anterior = pai[no_atual]
            gargalo = min(gargalo, residual[no_anterior][no_atual])
            no_atual = no_anterior

        no_atual = destino
        while no_atual != origem:
            no_anterior = pai[no_atual]
            residual[no_anterior][no_atual] -= gargalo
            residual[no_atual][no_anterior] += gargalo
            no_atual = no_anterior

        fluxo_total += gargalo

    return fluxo_total
