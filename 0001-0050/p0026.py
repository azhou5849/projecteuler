"""
Factors of 2 or 5 have no effect on the period, so we can focus on numbers ending in 1, 3, 7, 9
Once we make this assumption, the period of the decimal expansion of 1/d is the order of 10 modulo d
"""
best_denom = 1
max_period = 1

d = 3
while d < 1000:
    m, p = 10 % d, 1
    while m != 1:
        m = (10 * m) % d
        p += 1
    if p > max_period:
        best_denom = d
        max_period = p
    d += (4 if d % 10 == 3 else 2)  # stay on odds, skip numbers ending in 5

print(best_denom)
