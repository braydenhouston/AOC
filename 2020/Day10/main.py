# Day 10

file = open('input.txt')
adapters = file.read().split("\n")
file.close()

adapters = list(map(int, adapters))
adapters.sort()

diff = []
jolt = 0
for i in adapters:
    diff.append(i-jolt)
    jolt = i

print("Part 1 {}: ".format(diff.count(1) * (diff.count(3) + 1)))  # Off by 1 on 3 count....somehow
