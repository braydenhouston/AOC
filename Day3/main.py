with open('input.txt') as f:
    lines = f.readlines()

trees = [[]]*len(lines)
for pos, line in enumerate(lines, start=0):
    trees[pos] = [char for char in line.strip()]

col = 0
hits = 0

for row in range(0, len(trees)):
    if col >= len(trees[row]):
        col -= len(trees[row])

    if trees[row][col] == "#":
        hits += 1
        trees[row][col] = "X"
    else:
        trees[row][col] = "O"

    col += 3

for row in range(0, len(trees)):
    print(trees[row])

print("Part 1: {}".format(hits))


