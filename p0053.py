"""
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, C(5,3) = 10.
In general, C(n,r) = n! / (r! * (n - r)!).
It is not until n = 23, that a value exceeds one-million: C(23,10) = 1144066.
How many, not necessarily distinct, values of C(n,r) for 1 <= n <= 100, are greater than one-million?
-------------------------------
To find values of C(n,r), we can use Pascal's identity C(n,r) = C(n - 1, r) + C(n - 1, r - 1)
Also, for a fixed n, C(n,r) increases until r ~ n/2, then decreases, and C(n,r) = C(n, n - r).
    Therefore, we can find the smallest r such that C(n,r) > 1000000 then get the number of such r for the given value of n by using symmetry.
"""
N = 100

C = [[0 for r in range(N + 1)] for n in range(N + 1)]
C[0][0] = 1

total = 0
for n in range(1, N + 1):
    r = 0
    C[n][0] = 1
    while r <= n and C[n][r] <= 10**6:
        r += 1
        C[n][r] = C[n - 1][r] + C[n - 1][r - 1]
    if C[n][r] > 10**6:
        total += n - 2 * r + 1
print(total)
