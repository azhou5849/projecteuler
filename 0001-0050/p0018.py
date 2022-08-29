import math

triangle = []

f = open('p0018triangle.txt')
for line in f:
    triangle.append([int(n) for n in line.split()])
f.close()

maximums = [[0 for n in row] for row in triangle]

for i in range(-1, -len(maximums) - 1, -1):
    if i == -1:
        maximums[i] = triangle[i]
    else:
        for j in range(len(maximums[i])):
            maximums[i][j] = max(maximums[i + 1][j], maximums[i + 1][j + 1]) + triangle[i][j]

maximums[0][0]
