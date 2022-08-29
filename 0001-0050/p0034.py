"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
---------------------------
For a k-digit number, the largest possible such sum is k * 9! = 362880k < (10^6)k.
The smallest k-digit number is 10^(k - 1), so when 10^(k - 1) > (10^6)k, there are no k-digit solutions.
This occurs for all k >= 8, so we only need to check from 2-digit numbers through 7-digit numbers.
For 7-digit numbers, we more precisely only have to go up to 7 * 9!, which is substantially smaller than 9999999.
"""
def factorial(n):
    """
    Computes n! for a non-negative integer n
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial_list = [factorial(n) for n in range(10)]

def factorial_digit_sum(n):
    """
    Computes the sum of the factorials of the digits of a positive integer n
    """
    if n < 10:
        return factorial_list[n]
    else:
        return factorial_list[n % 10] + factorial_digit_sum(n // 10)

total = 0
for n in range(10, 7 * factorial_list[9]):
    if n == factorial_digit_sum(n):
        total += n
print(total)
