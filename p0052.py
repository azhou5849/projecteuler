"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
---------
x must have at least 3 digits, since the number of permutations of the digits must be at least 6.
"""
def is_permutation(m,n):
    """
    Checks if the digits of m are a permutation of the digits of n
    """
    m_digits = [int(c) for c in str(m)]
    n_digits = [int(c) for c in str(n)]
    return sorted(m_digits) == sorted(n_digits)

done = False
x = 100
while not done:
    m = 2
    while m <= 6:
        if not is_permutation(x, m * x):
            x += 1
            break
        m += 1
    if m == 7:
        done = True
print(x)
