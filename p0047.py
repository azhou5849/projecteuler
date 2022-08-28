"""
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""
import timeit
start = timeit.default_timer()

def prime_factors(n):
    """
    Returns a list of the distinct prime factors of n > 2
    """
    d, m = 2, n
    primes = []
    while m >= d * d:
        if m % d == 0:
            m = m // d
            if len(primes) == 0 or d != primes[-1]:
                primes.append(d)
        else:
            d += 1
    primes.append(m)
    return primes

done = False
n = 210
while not done:
    if len(prime_factors(n)) != 4:
        n += 1
        continue
    if len(prime_factors(n + 1)) != 4:
        n += 2  # can skip over n + 1
        continue
    if len(prime_factors(n + 2)) != 4:
        n += 3  # can skip over n + 1 and n + 2
        continue
    if len(prime_factors(n + 3)) != 4:
        n += 4  # can skip over n + 1, n + 2, and n + 3
        continue
    done = True
print(n)

stop = timeit.default_timer()
print('Time: ', stop - start)
