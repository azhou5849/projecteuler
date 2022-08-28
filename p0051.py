"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
----------
To avoid divisibility by 3, the number of replacement spots must be divisible by 3 by pigeonhole.
    Then the leftover digits cannot form a number divisible by 3 either.
The units digit cannot be one of the replacement spots.
"""
from math import inf
from sympy import isprime

def subsets(lst, k):
    """
    Return a list of all subsets of lst of size k
    """
    if k > len(lst):
        return []
    elif k == 0:
        return [[]]
    else:
        return subsets(lst[1:], k) + [[lst[0]] + S for S in subsets(lst[1:], k - 1)]

no_more_digits = False
n_digits = 4
best = inf
while not no_more_digits:
    possible_reps = []  # possible replacement digit sets, with index 0 being the left-most digit
    for k in range(3, n_digits, 3):
        possible_reps += subsets(list(range(n_digits - 1)), k)
    for S in possible_reps:
        remaining_digits = n_digits - len(S)
        lower_limit = 0
        if 0 not in S:
            lower_limit = 10 ** (remaining_digits - 1)
        for i in range(lower_limit, 10 ** remaining_digits):
            if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
                continue
            replace_into = ""
            i_str = str(i).zfill(remaining_digits)
            counter = 0
            for d in range(n_digits):
                if d in S:
                    replace_into += "*"
                else:
                    replace_into += i_str[counter]
                    counter += 1
            prime_count = 0
            min_first_digit = int(0 in S)
            for r in range(min_first_digit, 10):
                n = int(replace_into.replace('*', str(r)))
                if isprime(n):
                    if prime_count == 0:
                        candidate = n
                    prime_count += 1
            if prime_count >= 8:
                no_more_digits = True
                if candidate < best:
                    best = candidate
    n_digits += 1
print(best)
