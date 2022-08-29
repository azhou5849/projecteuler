import math

num_list = []

f = open("p0013list.txt")
for line in f:
    num_list.append(int(line))
f.close()

sum(num_list)
