# Day 8


file = open('input.txt')
instructions = file.read().split("\n")
file.close()

crumbs = []
line = 0
acc = 0
while True:
    op, arg = instructions[line].split(" ")
    arg = int(arg)

    if crumbs.count(line) > 0:
        break

    crumbs.append(line)

    if op == "acc":
        acc += arg
        line += 1
    elif op == "jmp":
        line += arg
    elif op == "nop":
        line += 1

print("Loop found at line: {} with value: {}".format(line, acc))