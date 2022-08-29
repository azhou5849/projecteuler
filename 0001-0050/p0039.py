"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?
--------------------
Every pythagorean triple can be uniquely written in the form k(m^2 - n^2), 2kmn, k(m^2 + n^2) with m > n, gcd(m,n) = 1, and m,n of opposite parity
The perimeter is p = 2km(m + n), so p is even, then we want the number of solutions to km(m + n) = s, where s = 0, 1, 2, ..., 500 is the semiperimeter
"""
from math import gcd

num_solutions = [0 for _ in range(501)]

k = 1
while k <= 83:  # m(m + n) >= 6 so k < 500/6 = 83.333....
    n = 1
    while k * (n + 1) * (2 * n + 1) <= 500:  # m >= n + 1
        m = n + 1
        while k * m * (m + n) <= 500:
            if gcd(m,n) == 1:
                num_solutions[k * m * (m + n)] += 1
            m += 2
        n += 1
    k += 1

print(2 * num_solutions.index(max(num_solutions)))
