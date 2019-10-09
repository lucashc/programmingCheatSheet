# Longest increasing subsequence
def longest_sub(arr): #length only
  res = []
  for i in arr:
    p = bisect_left(res, i)
    if p < len(res):
      res[p] = i
    else:
      res += [i]
  return len(res)
#other
from collections import namedtuple 
from functools import total_ordering
from bisect import bisect_left
 
@total_ordering
class Node(namedtuple('Node_', 'val back')):
    def __iter__(self):
        while self is not None:
            yield self.val
            self = self.back
    def __lt__(self, other):
        return self.val < other.val
    def __eq__(self, other):
        return self.val == other.val
 
def lis(d):
    """Return one of the L.I.S. of list d using patience sorting."""
    if not d:
        return []
    pileTops = []
    for di in d:
        j = bisect_left(pileTops, Node(di, None))
        #bisect right for non-strictly
        new_node = Node(di, pileTops[j-1] if j > 0 else None)
        if j == len(pileTops):
            pileTops.append(new_node)
        else:
            pileTops[j] = new_node
 
    return list(pileTops[-1])[::-1]
