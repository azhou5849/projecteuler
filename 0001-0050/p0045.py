"""
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.
Find the next triangle number that is also pentagonal and hexagonal.
----------------------
Note that T_(2n + 1) = H_(n + 1), so we just need to look for the first hexagonal number after H_143 that is also pentagonal
If P_n = H_m, then 3n^2 - n = 2m(2m - 1) -> n = [1 + sqrt(1 + 24m(2m - 1))] / 6
Thus we need 48m^2 - 24m + 1 = 3(4m - 1)^2 - 2 to be a perfect square, say x^2 = 3y^2 - 2 for y = 4m - 1, and x needs to be 5 modulo 6 for n to be an integer
Then we are looking for solutions to x^2 - 3y^2 = -2
The Pell equation x^2 - 3y^2 = 1 has basic solution (2,1) corresponding to the factorisation
    (2 + sqrt(3))(2 - sqrt(3)) = 1.
The equation we are looking to solve has solution (1,1) [call this solution 0], corresponding to
    (1 + sqrt(3))(1 - sqrt(3)) = -2.
We can thus get any solution to x^2 - 3y^2 = -2 by multiplying 1 + sqrt(3) repeatedly by 2 + sqrt(3) and reading off the coefficients.
If a + b sqrt(3) is a solution, then the next one is (2a + 3b) + (a + 2b) sqrt(3).
Note that we need y to be 3 modulo 4, so tracking what happens to solutions modulo 4 and modulo 6 is helpful:
    0: (1,1)      (1,1) mod 4 and (1,1) mod 6
    1: (5,3)      (1,3) mod 4 and (5,3) mod 6  <--- this corresponds to T1 = P1 = H1 = 1
    2: (19,11)    (3,3) mod 4 and (1,5) mod 6
    3: (71,41)    (3,1) mod 4 and (5,5) mod 6
    4: (265,153)  (1,1) mod 4 and (1,3) mod 6
    5: (989,571)  (1,3) mod 4 and (5,1) mod 6  <--- this corresponds to the given solution
    6: ~~~~~~~~~  (3,3) mod 4 and (1,1) mod 6
Thus we see that the periods mod 4 and mod 6 are 4 and 6, respectively, but more importantly, that x = 5 mod 6 and y = 3 mod 4 every four solutions.
As such, we want the 9th solution.
"""
class Solution:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.i = 0

    def next(self):
        self.i += 1
        self.x, self.y = 2 * self.x + 3 * self.y, self.x + 2 * self.y

    def jump(self, n = 1):
        for _ in range(n):
            self.next()

sol = Solution()
sol.jump(9)
n = (1 + sol.x) // 6
print(n * (3 * n - 1) // 2)
