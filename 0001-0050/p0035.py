"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
----------------------------------
Aside from the one-digit examples, the only allowed digits are 1, 3, 7, 9.
"""
import math

is_prime = [True for n in range(10**6)]
is_prime[0] = False
is_prime[1] = False
for n in range(2, 10**6):
    if is_prime[n]:
        for k in range(2, (10**6 - 1) // n + 1):
            is_prime[n * k] = False

def all_digits_in_list(n, digits):
    """
    Checks whether all digits of the positive integer n are in the set 'digits'
    """
    if n < 10:
        return (n in digits)
    else:
        return (n % 10 in digits) and all_digits_in_list(n // 10, digits)

def cycles(n):
    """
    Outputs a list of all rotations of the digits of n
    """
    num_digits = math.floor(math.log10(n)) + 1
    rotations = []
    temp = n
    for _ in range(num_digits):
        rotations.append(temp)
        temp = (temp % 10) * (10 ** (num_digits - 1)) + (temp // 10)
    return rotations

circular = [2, 3, 5, 7]
for n in range(10, 1000000):
    if all_digits_in_list(n, [1, 3, 7, 9]) and n not in circular:
        rotations = cycles(n)
        is_circular = True
        for p in rotations:
            if not is_prime[p]:
                is_circular = False
        if is_circular:
            circular.append(n)
print(len(circular))
