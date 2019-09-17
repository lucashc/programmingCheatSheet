# Max Flow (Ford-Fulkerson)
## \note Using a matrix $g$ with source $s$ and sink $t$
from queue import Queue
import math
def max_flow(s, t, g):
    m = 0
    path = bfs(s, t, g)
    while path[t] != -1:
        flow = math.inf
        current = t
        while current != s:
            flow = min(flow, g[path[current]][current])
            current = path[current]
        current = t
        while current != s:
            g[path[current]][current] -= flow
            g[current][path[current]] += flow
            current = path[current]
        m += flow
        path = bfs(s, t, g)
    return m

def bfs(s, t, g):
    visited = [False for i in range(len(g))]
    q = Queue()
    q.put(s)
    visited[s] = True
    path = [-1 for i in range(len(g))]
    while not q.empty():
        n = q.get()
        if n == t: break
        for i in range(len(g)):
            if not visited[i] and g[n][i] > 0:
                q.put(i)
                path[i] = n
                visited[i] = True
    return path
