import math

triangle = []

f = open('p0018triangle.txt')
for line in f:
    triangle.append([int(n) for n in line.split()])
f.close()

triangle
