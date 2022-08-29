"""
When b is not prime, we get f(0) = b is not prime, so this certainly does not pan out
When b is prime, f(b) is divisible by b, so it is not prime unless f(b) = b
    This can only happen if a = -b, in which case f(n) = n^2 - bn + b and f(1) = 1 is not prime
    Hence the maximum number of primes we could start with is b, namely f(0) through f(b - 1)
The bounds |a| < 1000 and |b| <= 1000 tell us that the largest primes that can possibly show up are at most 1,000,000
"""

# build list of primes up to 1,000,000
is_prime = [True for _ in range(1000000)]
is_prime[0] = False
is_prime[1] = False
for n in range(1000000):
    if is_prime[n]:
        for m in range(2, 999999 // n + 1):
            is_prime[m * n] = False
prime_list = [n for n in range(1000000) if is_prime[n]]

def in_sorted(sorted_list, item):
    """
    Implements binary search to test whether the number item is in sorted_list
    """
    if len(sorted_list) == 0:
        return False
    midpoint = len(sorted_list) // 2
    if sorted_list[midpoint] == item:
        return True
    else:
        if len(sorted_list) == 1:
            return False
        elif sorted_list[midpoint] < item:
            if len(sorted_list) == 2:
                return False
            else:
                return in_sorted(sorted_list[midpoint + 1 : ], item)
        else:
            return in_sorted(sorted_list[:midpoint], item)

def primes_up_to_n(n):
    return [p for p in prime_list if p < n]

most_primes = 0
best_tuple = (0,0)  # (a,b)
for b in primes_up_to_n(1000): # ensure f(0) is prime
    print(b)
    for a in [p - b - 1 for p in primes_up_to_n(2000) if p - b - 1 < 1000]:  # ensure f(1) is prime
        def f(n):
            return (n ** 2) + (a * n) + b
        n = 2
        while f(n) > 1 and in_sorted(prime_list, f(n)):
            n += 1
        if n > most_primes:
            most_primes = n
            best_tuple = (a, b)

print(most_primes)
print(best_tuple)
