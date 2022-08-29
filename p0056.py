"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""
max_sum = 0
for a in range(1,100):
    for b in range(1,100):
        digit_sum = sum([int(c) for c in str(a ** b)])
        if digit_sum > max_sum:
            max_sum = digit_sum
print(max_sum)
