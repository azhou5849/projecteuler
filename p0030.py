"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
------------------------------------------------------
For a k-digit number, the largest possible digit sum is
k * 9^5 < 100000k
while the k-digit number must be at least 10^(k - 1). When k > 6, we have 10^(k - 1) > 100000k, so we do not need to check numbers with more than 6 digits.
"""
fifth_powers = [n ** 5 for n in range(0,10)]

def sum_fifth_power_digits(n):
    """
    Computes the sum of the fifth powers of the digits of the positive integer n
    """
    if n == 0:
        return 0
    else:
        return fifth_powers[n % 10] + sum_fifth_power_digits(n // 10)

total = 0
for n in range(10,1000000):
    if n == sum_fifth_power_digits(n):
        total += n
print(total)
