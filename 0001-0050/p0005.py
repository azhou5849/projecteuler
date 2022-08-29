import math

def gcd(a,b):
    '''Takes in two positive integers and returns the gcd computed by the Euclidean algorithm'''
    if a > b:
        return gcd(b,a)
    elif a == 0:
        return b
    else:
        return gcd(b % a, a)

def lcm(a,b):
    '''Takes in two positive integers and returns the lcm by the relation ab = gcd(a,b) * lcm(a,b)'''
    return a * b / gcd(a,b)

mult = 1
for n in range(2,21):
    mult = lcm(mult, n)

print(mult)
