import math

collatz_chains = {1: 1}

def collatz(n):
    return int(n / 2) if n % 2 == 0 else 3 * n + 1

def chain_length(n):
    if collatz(n) in collatz_chains.keys():
        collatz_chains.update({n : 1 + collatz_chains.get(collatz(n))})
        return 1 + collatz_chains.get(collatz(n))
    else:
        k = chain_length(collatz(n))
        collatz_chains.update({n : 1 + k})
        return 1 + k

n_max_length, max_length = 1, 1
for n in range(2, 1000000):
    k = chain_length(n)
    if k > max_length:
        n_max_length, max_length = n, k

n_max_length
