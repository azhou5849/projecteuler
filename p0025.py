"""
By Binet's formula, if phi is the positive root of x^2 - x - 1, then F_n is the nearest integer to phi^n / sqrt(5).
Thus we want phi^n / sqrt(5) >= 10^999, or n log_10(phi) >= 999 + log_10(sqrt(5)) = 999 + 0.5 * log_10(5).
(One might worry about an edge case where phi^n / sqrt(5) rounds up to exactly 10^999, but this can be ruled out as follows.
Looking modulo 2 and 5, if F_n is divisible by 10, then n is divisible by 15. But F_15 = 610, so any F_n divisible by 10 is divisible by 61.)
"""
import math
phi = (1 + math.sqrt(5)) / 2
n = (999 + 0.5 * math.log10(5)) / (math.log10(phi))
print(math.ceil(n))
