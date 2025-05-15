def prim(graph):
    n = len(graph)
    selected = [False] * n
    key = [float('inf')] * n
    parent = [-1] * n

    key[0] = 0  # start from node 0

    for _ in range(n):
        # Rasti viršūnę su mažiausiu key reikšme
        min_key = float('inf')
        u = -1
        for v in range(n):
            if not selected[v] and key[v] < min_key:
                min_key = key[v]
                u = v

        selected[u] = True

        # Atnaujinti kaimynų key reikšmes
        for v in range(n):
            if graph[u][v] != 0 and not selected[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    # Surinkti rezultatus
    mst_edges = []
    total_weight = 0
    for v in range(1, n):
        mst_edges.append((parent[v], v, graph[parent[v]][v]))
        total_weight += graph[parent[v]][v]

    return total_weight, mst_edges

def main():
    # Adjacency matrix (0 reiškia nėra briaunos)
    graph = [
        [0, 2, 3, 0],
        [2, 0, 1, 1],
        [3, 1, 0, 4],
        [0, 1, 4, 0]
    ]

    weight, edges = prim(graph)
    print("Total MST weight:", weight)
    print("Edges in MST:", edges)

if __name__ == "__main__":
    main()