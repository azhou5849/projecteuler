"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
----------------------
We create an 8 x 201 grid, where the (i,j) entry (0 <= i < 8 and 0 <= j <= 200) indicates the number of ways to get value j using only coins 0, 1, ..., i (in increasing order of value, e.g. coin 5 is the 50p coin).
The j = 0 column is initialised to all 1's (the only way is to not use any coins).
We can then work in order of increasing j, then increasing i, with the (i,j) entry being the sum of the (i - 1, j) entry and the (i, j - *) entry, where * is the value of coin i. (If j < *, then we do not include that term.)
"""
values = [1, 2, 5, 10, 20, 50, 100, 200]
grid = [[0 for j in range(201)] for i in range(8)]
for j in range(201):
    for i in range(8):
        if j == 0:
            grid[i][j] = 1
        else:
            if i == 0:
                grid[i][j] = grid[i][j - 1]
            elif j < values[i]:
                grid[i][j] = grid[i - 1][j]
            else:
                grid[i][j] = grid[i - 1][j] + grid[i][j - values[i]]
print(grid[7][200])
