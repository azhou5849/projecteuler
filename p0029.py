"""
Consider all integer combinations of a^b for 2 <= a <= 5 and 2 <= b <= 5:

2^2=4, 2^3=8, 2^4=16, 2^5=32
3^2=9, 3^3=27, 3^4=81, 3^5=243
4^2=16, 4^3=64, 4^4=256, 4^5=1024
5^2=25, 5^3=125, 5^4=625, 5^5=3125
If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by a^b for 2 <= a <= 100 and 2 <= b <= 100?
--------------------------------------
The reason the answer is not just 99 * 99 is because of overlaps when perfect powers are used as the base
Any base which is not a perfect power and for which no perfect power (other than itself) appears in the list will contribute 99 terms that do not appear anywhere else
The remaining bases can be separated into sets based on what base we get when we re-write them to have smallest base possible,
e.g. 2, 4, 8, 16, 32, 64 all get grouped
"""
power_of = {2: (2,1), 4: (2,2), 8: (2,3), 16: (2,4), 32: (2,5), 64: (2,6),
            3: (3,1), 9: (3,2), 27: (3,3), 81: (3,4),
            5: (5,1), 25: (5,2),
            6: (6,1), 36: (6,2),
            7: (7,1), 49: (7,2),
            10: (10,1), 100: (10,2)}
exponents = { 2: [], 3: [], 5: [], 6: [], 7: [], 10: [] }  # record distinct exponents for each of these bases, e.g. 8^70 = 2^210, so we put 210 into 2's list

count = 0
for a in range(2,101):
    if a in power_of:
        min_base, exp = power_of[a]
        for b in range(2, 101):
            if exp * b not in exponents[min_base]:
                exponents[min_base].append(exp * b)
    else:
        count += 99
for base in exponents:
    count += len(exponents[base])
print(count)