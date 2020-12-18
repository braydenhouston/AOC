# Day 15.2

payload = "10,16,6,0,1,17"

mem = payload.split(",")
lookup = {}

for pos, val in enumerate(mem[:-1]):
    lookup[val] = pos

for i in range(len(mem)-1, 30000000 - 1):
    if mem[i] not in lookup.keys():
        lookup[mem[i]] = len(mem) - 1
        mem.append("0")
    else:
        mem.append(str(i-lookup[mem[i]]))
        lookup[mem[i]] = i

print("Part 2: {}".format(mem[-1]))

