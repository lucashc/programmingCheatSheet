# Dijkstra's algorithm
## \note \ms{nodes} is a list with node $i$ at index $i$ and then this node contains a list of tuples that indicate the length of the edge and whereto.
def dijkstra(a, b, nodes):
    import heapq
    visited = {}
    q = [(0, a)]
    distances = [float('inf') for _ in range(len(nodes))]
    distances[a] = 0
    while q:
        _, current = heapq.heappop(q)
        if current not in visited:
            visited.add(current)
            if current == b: return distances[b]
            for w, n in nodes[current]:
                if n in visited: continue
                if distances[n] > w + distances[current]:
                    distances[n] = w + distances[current]
                    heapq.heappush((distances[n], n))
    return float('inf')
