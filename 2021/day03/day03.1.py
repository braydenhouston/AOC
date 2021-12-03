# Day 3.1

def binaryToDecimal(n):
    return int(n,2)

with open("input.txt") as input:
    lines = [line.strip() for line in input.readlines()]

gamma = ""
eps = ""
totals  = []

for l in lines[0]:
    totals.append([])

for l in lines:
    for i in range(0,len(l)):
        totals[i].append(l[i])

for i in totals:
    gamma = gamma + "" + max(set(i), key= i.count)
    eps = eps + "" + min(set(i), key= i.count)


print("Part 1:", binaryToDecimal(gamma) * binaryToDecimal(eps) )


