import math

f = open("p0011grid.txt")
grid = []
for line in f:
    numbers = [int(n) for n in line.strip().split(" ")]
    grid.append(numbers)
f.close()

max_prod = 0
for i in range(20):  # products along rows
    for j in range(17):
        prod = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
        max_prod = prod if prod > max_prod else max_prod
for i in range(17):  # products along columns
    for j in range(20):
        prod = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
        max_prod = prod if prod > max_prod else max_prod
for i in range(17):  # products along top left - bottom right diagonals
    for j in range(17):
        prod = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
        max_prod = prod if prod > max_prod else max_prod
for i in range(17):  # products along top right - bottom left diagonals
    for j in range(3,20):
        prod = grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3]
        max_prod = prod if prod > max_prod else max_prod

print(max_prod)
