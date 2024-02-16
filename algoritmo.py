import heapq

def algoritmo_dijkstra(grafo, inicio):
    distancias = {}
    
    for vertice in grafo:
        distancias[vertice] =  float('inf')
        
    distancias[inicio] = 0
    
    fila_de_prioridade = [(0, inicio)]
    
    while fila_de_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_de_prioridade)
        
        if distancia_atual > distancias[vertice_atual]:
            continue;
        
        for vizinho, peso in grafo[vertice_atual].items():
            distancia_acumulada = distancia_atual + peso
            
            if distancia_acumulada < distancias[vizinho]:
                distancias[vizinho] = distancia_acumulada
                heapq.heappush(fila_de_prioridade, (distancia_acumulada, vizinho))
        
    return distancias

grafo = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4, 'E': 2},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 2, 'D': 3, 'F': 7},
    'F': {'D': 6, 'E': 7}
}

inicio = 'A'

distancias = algoritmo_dijkstra(grafo, inicio)

print("Distâncias mínimas a partir do vértice inicial {}: {}".format(inicio, distancias))