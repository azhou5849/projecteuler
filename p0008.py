import math

f = open("p0008number.txt", "r")
n_string = ""
for line in f:
    n_string = n_string + line.strip()
f.close()

max_prod = 0
substr_len = 13
for i in range(0, len(n_string) - substr_len + 1):
    prod = 1
    for j in range(0, substr_len):
        prod = prod * int(n_string[i + j])
    if prod > max_prod:
        max_prod = prod

print(max_prod)
