# Primality check and factorisation
## \note Changing \ms{return False} to \ms{print(i)} shows all prime factors of $n$ 
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1):
        if n % i == 0: 
            return False
    return True

