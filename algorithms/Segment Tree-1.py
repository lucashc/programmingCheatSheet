# Segment Tree
class SegmentTree:
    def __init__(s, l):
        s.n = len(l)
        s.tree = [0] * s.n + list(l)
        for i in range(s.n - 1, 0, -1):
            s.tree[i] = s.tree[2*i] + s.tree[2*i + 1]

    def update(s, p, val):
        p += s.n
        s.tree[p] = val
        while p > 1:
            p >>= 1
            s.tree[p] = s.tree[2*p] + s.tree[2*p + 1] #sum segment tree
            # s.tree[p] = max(s.tree[2*p], s.tree[2*p + 1]) # max segment tree
            

    def query(s, l, r): # interval [l, r)
        l += s.n; r += s.n
        t = 0
        while l < r:
            if l&1:
                t += s.tree[l] # r = max(res, tree[l])
                l += 1
            if r&1:
                r -= 1
                t += s.tree[r] # r = max(res, tree[r])
            l //= 2; r //= 2
        return t
        
