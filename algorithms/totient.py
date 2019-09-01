# Euler's totient function
def totient(n):
    ans = n
    i = 2
    while i**2 <= n:
        if n % i == 0: ans -= ans / i
        while n % i == 0: n /= i
        i += 1
    if n > 1: ans -= ans / n
    return ans

