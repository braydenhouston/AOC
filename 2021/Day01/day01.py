# Day 1.1
with open("input.txt") as input:
    lines = [int(line.strip()) for line in input.readlines()]

up = 0
for l in range(1, len(lines)):
    if lines[l] >= lines[l-1]:
        up += 1
    else:
        continue

print("Part 1: ", up)
