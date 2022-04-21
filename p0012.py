import math

def num_divisors(n):
    '''Returns the number of divisors of a positive integer'''
    count = 0
    r = math.isqrt(n)
    for d in range(1,r):
        count = count + (2 if n % d == 0 else 0)
    return count + (r * r == n)

num_divisors(140)
