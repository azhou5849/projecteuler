"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
------------------------------------------------
5-digit products are impossible: we have only 4 digits left, but (1 digit)(3 digit) < 9 * 999 < 10000 and (2 digit)(2 digit) < 99^2 < 10000.
3-digit products are impossible: we have 6 digits left and the product is at least as large as the individual factors, so the only case we could look at would be (3 digit)(3 digit) > 100 * 100 = 10000.
For 4-digit products, we have the possibilities (1 digit)(4 digit) and (2 digit)(3 digit).
    For the first case, note that the 1-digit number cannot be 1 or 9 (in the latter, the first digit of the product has to be 9).
"""
def digits(n):
    """
    Extract the digits of the positive integer n as a list
    """
    if n == 0:
        return []
    else:
        return digits(n // 10) + [n % 10]

def list_overlap(l_1, l_2):
    for x in l_1:
        if x in l_2:
            return True
    return False

pandigital_products = []
for a in range(2,9):
    for b in range(1234, 9999 // a):
        digits_b = digits(b)
        if list_overlap([0,a], digits_b):
            continue
        digits_p = digits(a * b)
        if list_overlap([0,a] + digits_b, digits_p):
            continue
        pandigital_products.append(a * b)
print(pandigital_products)
