# Day 1.2
with open("input.txt") as input:
    lines = [int(line.strip()) for line in input.readlines()]

totals = []
for l in range(len(lines)):
    totals.append(sum(lines[l:l + 3]))

largerCount = 0
for i in range(1, len(totals)):
    if totals[i] > totals[i - 1]:
        largerCount += 1

print("Part 1: ", largerCount)
