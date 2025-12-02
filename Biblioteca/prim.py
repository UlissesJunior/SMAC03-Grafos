def prim(matriz):
    num_vertices = len(matriz)
    selecionados = {0}          
    arestas_mst = []           
    peso_total = 0

    while len(selecionados) < num_vertices:
        melhor_aresta = None

        for v in selecionados:
            for u in range(num_vertices):
                peso = matriz[v][u]

                if peso != 0 and u not in selecionados:
                    if melhor_aresta is None or peso < melhor_aresta[2]:
                        melhor_aresta = (v, u, peso)

        arestas_mst.append((melhor_aresta[0], melhor_aresta[1]))
        peso_total += melhor_aresta[2]
        selecionados.add(melhor_aresta[1])

    print(arestas_mst, peso_total)

prim([[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]])