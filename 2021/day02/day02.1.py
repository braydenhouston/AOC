# Day 2.1
with open("input.txt") as input:
    lines = [line.strip() for line in input.readlines()]

hoz = 0
depth = 0

for line in lines:
    [cmd, amt] = line.split(" ")

    if cmd == "forward":
        hoz = hoz + int(amt)
    elif cmd == "up":
        depth = depth - int(amt)
    elif cmd == "down":
        depth = depth + int(amt)


print("Part 1: ", hoz * depth)
