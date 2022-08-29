"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
-----------------------------------------------------------------------------------------------------------------------
On the n-th layer out from the center, where layer 1 has numbers 2 through 9, the average of the corners is the center left entry
(e.g. average of 3, 5, 7, 9 is 6; average of 13, 17, 21, 25 is 19)
For a 1001 x 1001 spiral, there are 500 layers
The center left entry of layer n is a quadratic function of n, given by (2n + 1)^2 - 2n - n = 4n^2 + n + 1
    Start from the upper right and go backwards (2n for the top row, then n for half the left side)
Thus we need 1 + sum from n = 1 to 500 of 4(4n^2 + n + 1)
"""
1 + sum([4 * (4 * n * n + n + 1) for n in range(1, 501)])
