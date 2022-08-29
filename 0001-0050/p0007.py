import math

primes = [2]
n = 3

def is_prime(primes, n):
    return not any([n % p == 0 for p in primes if p * p <= n])

while len(primes) < 10001:
    if is_prime(primes, n):
        primes.append(n)
    n = n + 2

print(primes[10000])
