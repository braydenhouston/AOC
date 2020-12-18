# Day 14

file = open('input.txt')
payload = file.read().split("\n")
file.close()


def bitmagic(mask, value):
    value = bin(int(value)).split('b')[1]
    value = value.zfill(36)

    result = []
    for i in range(0, len(mask)):
        if mask[i] == "X":
            result.append(value[i])
        else:
            result.append(mask[i])

    result = ''.join(result)
    result = int(result, 2)
    return result


mem = {}
mask = ""
for line in payload:
    cmd, value = line.split(" = ")
    # print("{} {}".format(cmd, value))

    if cmd == "mask":
        mask = value

    elif cmd[:3] == "mem":
        mem[cmd[4:-1]] = bitmagic(mask, value)

print("Part 1: {}".format(sum(mem.values())))
