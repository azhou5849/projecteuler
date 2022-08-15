import math

def sum_divisors(n):
    """
    Returns the sum of all positive divisors of a positive integer n
    """
    sum = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            sum += d
            if n // d != d:  # avoid double-counting for a perfect square
                sum += n // d
        d += 1
    return sum

abundant_numbers = [n for n in range(1,28123) if sum_divisors(n) > 2 * n]

is_sum = [0 for _ in range(28125)]  # 0 when not a sum, > 0 otherwise
for i in range(len(abundant_numbers)):
    for j in range(i + 1):
        m = abundant_numbers[i] + abundant_numbers[j]
        if m > 28123:
            break
        is_sum[m] += 1

total = 0
for n in range(1, 28124):
    if is_sum[n] == 0:
        total += n

print(total)
