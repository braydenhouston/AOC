# Day 10

file = open('input.txt')
adapters = file.read().split("\n")
file.close()

adapters = list(map(int, adapters))
adapters.append(0)
adapters.sort()

diff = []
jolt = 0
for i in adapters:
    diff.append(i-jolt)
    jolt = i

print("Part 1: {}".format(diff.count(1) * (diff.count(3) + 1)))

alen = len(adapters)
diff = [0] * alen
diff[0] = 1

for x in range(1, alen):
    for y in range(x):
        if adapters[x] - adapters[y] <= 3:
            diff[x] += diff[y]

print("Part 2: {}".format(diff[alen - 1]))
