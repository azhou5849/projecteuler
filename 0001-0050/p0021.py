import math

def sum_proper_divisors(n):
    """
    Compute the sum of the positive proper divisors of an integer n > 1
    """
    sum_divisors = 0
    d = 1
    while d * d <= n:  # each divisor below sqrt(n) pairs with one above sqrt(n)
        if n % d == 0:
            sum_divisors += d
            if n // d not in [d, n]:  # do not double-count (if n is a perfect square) or include n (not a perfect divisor)
                sum_divisors += (n // d)
        d += 1
    return sum_divisors

amicable = []
for n in range(2, 10000):
    m = sum_proper_divisors(n)
    if m != n and sum_proper_divisors(m) == n:
        amicable.append(n)
print(sum(amicable))
