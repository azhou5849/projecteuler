import math

def divisors(n):
    '''Returns a list of the divisors of n'''
    return [d for d in range(1, n + 1) if n % d == 0]

s = 500  # semiperimeter
triples = []
for k in divisors(s):
    r = int(500 / k)
    for m in divisors(r):
        if r / m > m and r / m < 2 * m:
            n = int(r / m) - m
            triples.append([k * (m * m - n * n), k * (2 * m * n), k * (m * m + n * n)])

print([a * b * c for [a,b,c] in triples])
