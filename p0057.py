"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.
The first seven expansions are
    3/2
    7/5
    17/12
    41/29
    99/70
    239/169
    577/408
The eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
-------------------------------------------------
From continued fraction theory, the numerators p(n) and denominators q(n) satisfy the recurrence
    p(0) = 1
    q(0) = 1
    p(n) = p(n - 1) + 2 * q(n - 1)
    q(n) = p(n - 1) + q(n - 1)
By the euclidean algorithm, p(n)/q(n) is always already in lowest terms.
"""
count = 0
p, q = 1, 1
for _ in range(1000):
    p, q = p + 2 * q, p + q
    if len(str(p)) > len(str(q)):
        count += 1
print(count)
