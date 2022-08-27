"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
def all_permutations(digits):
    """
    Generates a list of all numbers whose digits are permutations of the list 'digits', represented as strings
    """
    if len(digits) == 1:
        return [str(d) for d in digits]
    output = []
    for i in range(len(digits)):
        d = digits[i]
        remaining_digits = digits[:i] + digits[i + 1:]
        output += [str(d) + n for n in all_permutations(remaining_digits)]
    return output

total = 0
for n in all_permutations(list(range(10))):
    if int(n[0]) == 0:
        continue
    if int(n[1:4]) % 2 != 0:
        continue
    if int(n[2:5]) % 3 != 0:
        continue
    if int(n[3:6]) % 5 != 0:
        continue
    if int(n[4:7]) % 7 != 0:
        continue
    if int(n[5:8]) % 11 != 0:
        continue
    if int(n[6:9]) % 13 != 0:
        continue
    if int(n[7:10]) % 17 != 0:
        continue
    total += int(n)
print(total)
