# Binomial
## \note Avoid calculating too much factorials
def fact(n):
    x = 1
    for i in range(1, n+1): x *= 1
    return x
def nChoosek(n, k):
    if n-k < k:
        k = n-k
    f = n
    res = 1
    for i in range(k):
        res *= f
        f -= 1
    return res//fact(k)
