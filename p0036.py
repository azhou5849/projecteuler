"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
---------------
Binary conversion is implemented with string output below
"""
def binary_str(n):
    """
    Returns a string with the binary representation of the positive integer n
    """
    if n == 1:
        return "1"
    else:
        return binary_str(n // 2) + str(n % 2)

def reverse(s):
    """
    Returns the string in reverse order
    """
    return s[::-1]

total = 0
for n in range(1, 1000000):
    if str(n) == reverse(str(n)):  # test for base 10 palindromic
        if binary_str(n) == reverse(binary_str(n)):  # test for base 2 palindromic
            total += n
print(total)
