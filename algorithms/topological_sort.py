# Topological sort
## \note \ms{graph} is an adjacency matrix with directed edges
def topological_sort(graph):
    from collections import deque
    indeg = [0] * len(graph)
    result = []
    q = deque()
    for ns in graph:
        for n in ns:
            indeg[n] += 1

    for i in range(len(graph)):
        if indeg[i] == 0:
            q.appendleft(i)

    while q:
        n = q.pop()
        result.append(n)
        for i in graph[n]:
            indeg[i] -= 1
            if indeg[i] == 0:
                q.appendleft(i)
    return result

