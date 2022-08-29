import math

for a in range(9,0,-1):
    for b in range(9,-1,-1):
        for c in range(9,-1,-1):
            n = 100001 * a + 10010 * b + 1100 * c

            d = 999
            while d > n / 1000:
                if n % d == 0:
                    print(n)
                    break
                else:
                    d = d - 1
