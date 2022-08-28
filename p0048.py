"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
def summod(n_list, mod):
    total = 0
    for n in n_list:
        total = (total + n) % mod
    return total

def powmod(base, exp, mod):
    result = 1
    for _ in range(exp):
        result = (result * base) % mod
    return result

print(summod([powmod(n, n, 10**10) for n in range(1, 1001)], 10**10))
