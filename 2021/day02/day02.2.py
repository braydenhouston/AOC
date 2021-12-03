# Day 2.1
with open("input.txt") as input:
    lines = [line.strip() for line in input.readlines()]

hoz = 0
depth = 0
aim = 0

for line in lines:
    [cmd, amt] = line.split(" ")

    if cmd == "forward":
        hoz = hoz + int(amt)
        depth = depth + ( aim * int(amt) )
    elif cmd == "up":
        aim = aim - int(amt)
    elif cmd == "down":
        aim = aim + int(amt)


print("Part 2: ", hoz * depth)
