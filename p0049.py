"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?
"""
is_prime = [True for _ in range(10000)]
is_prime[0] = False
is_prime[1] = False
for n in range(2, 10000):
    if is_prime[n]:
        m = 2 * n
        while m < 10000:
            is_prime[m] = False
            m += n
primes_4 = [n for n in range(1000, 10000) if is_prime[n]]

def is_permutation(m,n):
    """
    Checks if the digits of m are a permutation of the digits of n
    """
    m_digits = [int(c) for c in str(m)]
    n_digits = [int(c) for c in str(n)]
    return sorted(m_digits) == sorted(n_digits)

for i in range(len(primes_4) - 1):
    p = primes_4[i]
    for j in range(i + 1, len(primes_4)):
        q = primes_4[j]
        n = 2 * q - p
        if n >= 10000:
            continue
        else:
            if is_prime[n]:
                if is_permutation(p,q) and is_permutation(p,n):
                    print(str(p) + str(q) + str(n))
