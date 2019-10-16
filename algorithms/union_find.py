# Union Find
## \note Union find as used in Kruskal's minimum spanning tree.
class UnionFind:
    
    def __init__(self, nodes):
        self.nodes = list(range(nodes))
        self.rank = [0]*nodes
    def union(self, x, y):
        rootx = self.nodes[x]
        rooty = self.nodes[y]
        if self.rank[rootx] > self.rank[rooty]:
            self.nodes[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]:
            self.nodes[rootx] = rooty
        elif rootx != rooty:
            self.nodes[rooty] = rootx
            self.rank[rootx] += 1
    
    def find(self, x):
        if self.nodes[x] == x:
            return x
        self.nodes[x] = self.find(self.nodes[x])
        return self.nodes[x]
