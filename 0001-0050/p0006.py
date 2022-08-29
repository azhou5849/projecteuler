import math

def sum_of_square(n):
    '''Returns the sum of the first n squares, using the formula n * (n + 1) * (2 * n + 1) / 6'''
    return n * (n + 1) * (2 * n + 1) / 6

def sum_first_n(n):
    '''Returns the sum of the first n positive integers, using the formula n * (n + 1) / 2 '''
    return n * (n + 1) / 2

n = 100
print(sum_first_n(n) * sum_first_n(n) - sum_of_square(n))
