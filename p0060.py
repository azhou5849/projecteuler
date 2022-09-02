"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
-----------------------------------------
We build a graph where each node is a prime number and we draw an edge p -> q if the concatenation pq is prime
We are looking for a complete directed graph on 5 nodes
"""
import numpy as np

def count_clique(adj, k):
    """
    Given a graph specified by the adjacency matrix adj, and a positive integer k,
    count the number of k-cliques in the graph.
    """
    rows, cols = adj.shape
    if k == 3:
        square = np.matmul(adj, adj)
        return np.sum(np.multiply(adj, square)) // 6
    else:
        return "potato"

d = 3  # number of digits to work up to for nodes (so we need primes up to 2d digits), adjust as needed
is_prime = [True for _ in range(10 ** (2 * d))]
is_prime[0] = False
is_prime[1] = False
for n in range(2, 10 ** (2 * d)):
    if is_prime[n]:
        m = 2 * n
        while m < 10 ** (2 * d):
            is_prime[m] = False
            m += n
primes = [p for p in range(10 ** d) if is_prime[p]]

adj = np.zeros((len(primes), len(primes)), dtype = int)
for i in range(len(primes) - 1):
    for j in range(i + 1, len(primes)):
        n = int(str(primes[i]) + str(primes[j]))
        m = int(str(primes[j]) + str(primes[i]))
        if is_prime[n] and is_prime[m]:
            adj[i,j] = 1
            adj[j,i] = 1

count_clique(adj, 3)
