"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
---------------------------
Left and right truncatability can be checked by building up from previously left or right trunctable primes
The problem does tell us that we can stop once we find 11 primes which are both left and right truncatable, but for completeness, this program shows that there are only 11.
Every digit but the left-most must be in the set {1, 3, 7, 9} to avoid divisibility by 2 or 5
The left-most digit must be in the set {2, 3, 5, 7} in order to get a prime at the end when truncating from right to left
The right-most digit must be in the set {3, 7} in order to get a prime at the end when truncating from left to right
"""
from sympy import isprime

left_truncatable  = {1: [3, 7]}  # possible last digits
right_truncatable = {1: [2, 3, 5, 7]}  # possible first digits
both_truncatable  = {}  # stores final answer but does not appear in the building-up process

d = 1  # number of digits in first truncation
total = 0
while d == 1 or (len(left_truncatable[d]) > 0 and len(right_truncatable[d]) > 0):
    left_truncatable[d + 1] = []
    for base in left_truncatable[d]:
        for first_digit in [1, 2, 3, 5, 7, 9]:
            candidate = int(str(first_digit) + str(base))
            if isprime(candidate):
                left_truncatable[d + 1] = left_truncatable[d + 1] + [candidate]
    (left_truncatable[d + 1]).sort()

    right_truncatable[d + 1] = []
    for base in right_truncatable[d]:
        for last_digit in [1, 3, 7, 9]:
            candidate = int(str(base) + str(last_digit))
            if isprime(candidate):
                right_truncatable[d + 1] = right_truncatable[d + 1] + [candidate]
    (right_truncatable[d + 1]).sort()

    if len(left_truncatable[d + 1]) > 0 and len(right_truncatable[d + 1]) > 0:
        i,j = 0,0
        while i < len(left_truncatable[d + 1]) and j < len(right_truncatable[d + 1]):
            if left_truncatable[d + 1][i] == right_truncatable[d + 1][j]:
                total += left_truncatable[d + 1][i]
                i += 1
                j += 1
            elif left_truncatable[d + 1][i] > right_truncatable[d + 1][j]:
                j += 1
            else:
                i += 1

    d += 1

print(total)
