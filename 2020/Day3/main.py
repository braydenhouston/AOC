def sled(right, down):
    col = 0
    hits = 0
    for row in range(0, len(trees), down):
        if col >= len(trees[row]):
            col -= len(trees[row])

        if trees[row][col] == "#":
            hits += 1

        col += right
    # print("Right: {} Down: {} Hits: {}".format(right, down, hits))
    return hits


with open('input.txt') as f:
    lines = f.readlines()

trees = [[]]*len(lines)
for pos, line in enumerate(lines, start=0):
    trees[pos] = [char for char in line.strip()]

print("Part 1: {} hits".format(sled(3, 1)))

print("Part 2: {}".format(
    sled(1, 1) *
    sled(3, 1) *
    sled(5, 1) *
    sled(7, 1) *
    sled(1, 2)
))


