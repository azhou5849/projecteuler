import math

def positionless_score(name):
    return sum([ord(c) - 64 for c in name])

with open("p0022names.txt", 'r') as f:
    names_with_quotes = f.readline().strip().split(',')
    names = sorted([s.strip('"') for s in names_with_quotes])

total_score = 0
for i in range(len(names)):
    name = names[i]
    total_score += (i + 1) * positionless_score(name)
print(total_score)
