"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
----------------------------------
If (10a + b) / (10a + d) = b / d, then we get b = d and the example is trivial.
If (10a + b) / (10c + b) = a / c, then we get a = c and the example is trivial.
If (10a + b) / (10b + d) = a / d, then we get 10ad + bd = 10ab + ad, or 9ad + bd = 10ab.
    We can skip over cases where b = d or a = b, since those are covered above and are trivial.
    If a = d, then a = b is forced as well, so we get a trivial example.
    Also, d(b - a) = 0 mod 10, so either d = 5 and b - a is even or b - a = 5 and d is even. (We need b > a for the fraction to be less than 1.)
    If d = 5, then 45a + 5b = 10ab -> 9a + b = 2ab -> 18a + 2b = 4ab -> (2a - 1)(2b - 9) = 9 -> a = b = 5 (trivial) or a = 2 and b = 6 or a = 1 and b = 9:
        Solutions 26/65 = 2/5 and 19/95 = 1/5
    If b - a = 5, then b = a + 5 and so 9ad + (a + 5)d = 10a(a + 5) -> 10a^2 + 50a = 10ad + 5d -> 2a^2 + 10a = 2ad + d -> (2a^2 + 10a) / (2a + 1) = d
        After polynomial division, 2a + 1 divides 9a, and for a = 1, 2, 3, 4, this only happens when a = 1 (d = 4) and when a = 4 (d = 8)
        Solutions 16/64 = 1/4 and 49/98 = 4/8
The case (10a + b) / (10c + a) = b / c, then we get 10ac + bc = 10bc + ab, or 10ac = 9bc + ab.  (Note that we already found the four examples, but this case is included for completeness)
    Similar analysis to above shows that b = 5 and c - a is even or c - a = 5 and b is even.
    If b = 5, then 10ac = 45c + 5a -> 2ac = a + 9c -> 4ac - 2a - 18c = 0 -> (2a - 9)(2c - 1) = 9 -> no solutions with c > a
    If c - a = 5, then c = a + 5, so 10ac = 9bc + ab -> 10a^2 + 50a = 9ab + 45b + ab = 10ab + 45b -> 2a^2 + 10a = 2ab + 9b -> b = (2a^2 + 10a) / (2a + 9)
        After division, 2a + 9 divides a, but this is impossible
Hence we found all four solutions, and in lowest terms, the product is
    (2/5)(1/5)(1/4)(1/2) = (1/5)(1/5)(1/4) = 1/100.
"""
