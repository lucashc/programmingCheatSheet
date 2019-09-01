# Dijkstra's algorithm
## \note Replacing heapq with a priorityqueue from the \ms{queue}-package might be necessary
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
