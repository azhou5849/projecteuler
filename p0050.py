"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
is_prime = [True for _ in range(10**6)]
is_prime[0] = False
is_prime[1] = False
for n in range(2, 10**6):
    if is_prime[n]:
        m = 2 * n
        while m < 10**6:
            is_prime[m] = False
            m += n
primes = [p for p in range(10**6) if is_prime[p]]

best, length = 41, 6
for i in range(len(primes)):
    n = primes[i]
    l = 1
    for j in range(i + 1, len(primes)):
        n += primes[j]
        l += 1
        if n >= 10**6:
            break
        if is_prime[n] and l > length:
            best, length = n, l
print(best)
