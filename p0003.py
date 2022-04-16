import math

n = 600851475143
p = 3

while n > 1:
    if n % p == 0:
        n = n / p
    else:
        p = p + 2

print(p)
