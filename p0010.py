import math
from pyprimes import isprime

sum = 2
for n in range(3, 2 * pow(10,6), 2):
    sum = sum + (n if isprime(n) else 0)
print(sum)
