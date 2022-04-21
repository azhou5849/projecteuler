import math

def sum_of_digits(n_str):
    '''Computes the sum of digits in a positive integer, represented by a string n_str, by repeatedly shaving off digits'''
    if len(n_str) == 1:
        return int(n_str)
    else:
        return int(n_str[0]) + sum_of_digits(n_str[1:])

sum_of_digits(str(2 ** 1000))
