def kruskal_matriz(matriz):
    num_vertices = len(matriz)
    arestas = []

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if matriz[i][j] > 0:
                arestas.append((i, j, matriz[i][j]))

    arestas.sort(key=lambda x: x[2])
    
    pai = list(range(num_vertices)) 

    def find(v):
        while pai[v] != v:
            pai[v] = pai[pai[v]]   
            v = pai[v]
        return v

    agm = []  

    for origem, destino, peso in arestas:  
        raiz_origem = find(origem)
        raiz_destino = find(destino)

        if raiz_origem != raiz_destino:     
            agm.append((origem, destino, peso))  
            pai[raiz_destino] = raiz_origem      
            
            if len(agm) == num_vertices - 1:   
                break

    return agm