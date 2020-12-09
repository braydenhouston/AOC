# Day 8

def run(intruct):
    crumbs = []
    l = 0
    acc = 0
    while True:
        op, arg = intruct[l].split(" ")
        arg = int(arg)

        if crumbs.count(l) > 0:
            # print("Loop found at line: {} with value: {}".format(l, acc))
            return False

        crumbs.append(l)

        if op == "acc":
            acc += arg
            l += 1
        elif op == "jmp":
            l += arg
        elif op == "nop":
            l += 1

        if l >= len(intruct):
            print("Boot Successful with value: {}".format(acc))
            return True


file = open('input.txt')
instructions = file.read().split("\n")
file.close()

for pos in range(len(instructions)):
    line = instructions[pos].split(" ")

    if line[0] == "acc":
        continue

    test_instructions = instructions[:]

    if line[0] == "jmp":
        test_instructions[pos] = "{} {}".format("nop", line[1])
        print("Line {} changing {} to {}".format(pos, line[0], "nop"))
    else:
        test_instructions[pos] = "{} {}".format("jmp", line[1])
        print("Line {} changing {} to {}".format(pos, line[0], "jmp"))

    if run(test_instructions):
        break
