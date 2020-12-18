# Day 14.2

file = open('input.txt')
payload = file.read().split("\n")
file.close()


def runmask(value):
    if value.count("X") > 0:
        final.append(runmask(value.replace("X", "0", 1)))
        final.append(runmask(value.replace("X", "1", 1)))
    elif value.count("X") == 0:
        return value
    return


def bitmagic(mask, value, pos):
    bvalue = bin(int(pos)).split('b')[1]
    bvalue = bvalue.zfill(36)

    result = []
    for i in range(0, len(mask)):
        if mask[i] == "X":
            result.append("X")
        elif mask[i] == "0":
            result.append(bvalue[i])
        else:
            result.append(mask[i])

    result = ''.join(result)

    final.clear()
    runmask(result)
    addresses = list(filter(None, final))
    for addr in addresses:
        mem[int(addr, 2)] = int(value)
    return


mem = {}
final = []
mask = ""
for line in payload:
    cmd, value = line.split(" = ")

    if cmd == "mask":
        mask = value

    elif cmd[:3] == "mem":
        bitmagic(mask, value, cmd[4:-1])

print("Part 2: {}".format(sum(mem.values())))

