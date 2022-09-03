"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
-----------------------------------------
We build a graph where each node is a prime number and we draw an edge p -- q if the concatenations pq and qp are prime
We are looking for a K5 subgraph
"""
def list_cliques(n, edges, k):
    """
    Given a graph specified by the number of vertices n and dictionary 'edges' with keys 0, 1, ..., n - 1
    and sets edges[i] with j in edges[i] if and only if i and j are connected,
    and a positive integer k, return a list of all k-cliques in the graph.
    """
    if k == 1:
        return [[v] for v in range(n)]
    smaller_cliques = list_cliques(n, edges, k - 1)
    output = []
    for C in smaller_cliques:
        start = max(C) + 1  # this ensures that each clique is listed exactly once with vertices in increasing order
        for i in range(start, n):
            forms_clique = True
            for v in C:
                if v not in edges[i]:
                    forms_clique = False
                    break
            if forms_clique:
                output.append(C + [i])
    return output

d = 4  # number of digits to work up to for nodes (so we need primes up to 2d digits), adjust as needed
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

edges = {i: set() for i in range(len(primes))}
for i in range(len(primes) - 1):
    for j in range(i + 1, len(primes)):
        n = int(str(primes[i]) + str(primes[j]))
        m = int(str(primes[j]) + str(primes[i]))
        if is_prime[n] and is_prime[m]:
            edges[i].add(j)
            edges[j].add(i)

indices = list_cliques(len(primes), edges, 5)
print(indices)

for I in indices:
    print(sum([primes[i] for i in I]))
