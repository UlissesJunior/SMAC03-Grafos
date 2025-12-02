import math

def dijkstra(G, origem, destino):
    n = len(G)

    custo = [math.inf] * n
    rota  = [None] * n
    custo[origem] = 0
    rota[origem] = origem

    abertos  = list(range(n))
    fechados = []

    while abertos:
        atual = min(abertos, key=lambda v: custo[v])
        fechados.append(atual)
        abertos.remove(atual)

        vizinhos = [u for u in abertos if G[atual][u] > 0]

        for viz in vizinhos:
            novoCusto = custo[atual] + G[atual][viz]
            if novoCusto < custo[viz]:
                custo[viz] = novoCusto
                rota[viz] = atual

    caminho = []
    v = destino
    while v != origem:
        caminho.append(v)
        v = rota[v]
    caminho.append(origem)
    caminho.reverse()

    print(caminho, custo[destino])