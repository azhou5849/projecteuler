import math

def num_divisors(n):
    '''Returns the number of divisors of a positive integer'''
    count = 0
    r = math.isqrt(n)
    for d in range(1,r):
        count = count + (2 if n % d == 0 else 0)
    return count + (r * r == n)

d, n = 0, 0
while d <= 500:
    # we'll use the fact that d(n) is multiplicative
    n = n + 1
    d = num_divisors(int(n / 2)) * num_divisors(n + 1) if n % 2 == 0 else num_divisors(n) * num_divisors(int((n + 1) / 2))

print(int(n * (n + 1) / 2))
