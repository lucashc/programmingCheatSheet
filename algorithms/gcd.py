# Greatest common denominator
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b; b = c
    return a

