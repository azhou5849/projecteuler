"""
In f(n) = n^2 + an + b, when |b| != 1, we know that f(kd) is divisible by d, where d is any divisor of b and k >= 1
When |b| = 0 or |b| = 1, we get f(0) = b is not prime, so this certainly does not pan out

Otherwise, note that f(p), f(2p), f(3p) are all divisible by p, where p is the minimal prime divisor of b
The only way these can be prime is if they are equal to p, but since f is quadratic, only two of them can be equal to p
If f(p) = p, then calculating gives us a = 1 - p - b/p
    In this case, f(2p) = 4p^2 + 2p - 2p^2 - 2b + b = 2p^2 + 2p - b, and this equals p if and only if b = 2p^2 + p = p(2p + 1)
        In this case, a = 1 - p - (2p + 1) = -3p
        This forces 2p + 1 to be prime, otherwise it has a prime divisor smaller than p, contradicting minimality of p
        Also, we have f(n) = (n - p)(n - 2p) + p and then f(2p - 1) = 1 is not prime
The conclusion of this discussion is that we get at most 2p consecutive primes, f(0) through f(2p - 1)
    Unless specific conditions are met, we usually get at most p, f(0) through f(p - 1)

The bounds |a| < 1000 and |b| <= 1000 and |2p| < 2000 tell us that the largest primes that can possibly show up are at most 7,000,000
"""

# build list of primes up to 7,000,000
is_prime = [True for _ in range(7000000)]
is_prime[0] = False
is_prime[1] = False
for n in range(7000000):
    if is_prime[n]:
        for m in range(2, 6999999 // n + 1):
            is_prime[m * n] = False
prime_list = [n for n in range(7000000) if is_prime[n]]

def min_prime(n):
    """
    Get the minimum prime divisor of an integer n > 2
    """
    i = 0
    while prime_list[i] ** 2 <= n:
        if n % prime_list[i] == 0:
            return prime_list[i]
        i += 1
    return n

min_prime(79)
