"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
------------------------
The sum of the digits of an n-digit pandigital is n(n + 1) / 2.
This is divisible by 3 when n = 9 and n = 8, so the next place to check is when n = 7.
"""
from sympy import isprime

def all_permutations(digits):
    """
    Generates a list of all numbers whose digits are permutations of the list 'digits', sorted from largest to smallest
    """
    if len(digits) == 1:
        return digits
    output = []
    for i in range(len(digits)):
        d = digits[i]
        remaining_digits = digits[:i] + digits[i + 1:]
        output += [10 * n + d for n in all_permutations(remaining_digits)]
    return sorted(output, reverse = True)

pandigitals = all_permutations(list(range(1,8)))
for n in pandigitals:
    if isprime(n):
        print(n)
        break
