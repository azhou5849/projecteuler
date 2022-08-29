import math

def digit_sum(n):
    """
    Returns the digit sum of a non-negative integer n
    """
    if n < 10:
        return n
    else:
        return (n % 10) + digit_sum(n // 10)  # shave off the unit digit

def factorial(n):
    """
    Returns the value of n! = n * (n - 1) * ... * 1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(digit_sum(factorial(100)))
