import math

f_small, f_large, sum = 1, 1, 0
while f_large <= 4000000:
    f_small, f_large = f_large, f_small + f_large
    sum = sum + (f_large if f_large % 2 == 0 else 0)

print(sum)
