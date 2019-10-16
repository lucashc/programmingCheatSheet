# Fenwick Tree
## \note Efficiently calculate sums and update elements. The sum is taken from $0$ up to index \ms{r}. Updates happen with deltas and not with setting.
class FenwickSum:
    def __init__(self, items):
        self.items = [0 for _ in range(len(items))]
        self.size = len(items)
        for index, element in enumerate(items):
            self.update(index, element)
    def sum(self, r):
        if r < 0: return 0
        if r >= self.size: r = size - 1
        result = 0
        while r >= 0:
            result += self.items[r]
            r = (r & (r+1)) - 1
        return result
    def update(self, i, delta):
        while i < self.size:
            self.items[i] += delta
            i = i | (i+1)
