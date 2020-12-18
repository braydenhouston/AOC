# Day 15.1

payload = "10,16,6,0,1,17"

mem = payload.split(",")

for i in range(len(mem)-1, 2019):
    if mem[:-1].count(mem[i]) == 0:
        mem.append("0")
    else:
        temp = mem[:-1]
        res = len(temp) - 1 - temp[::-1].index(mem[i])
        mem.append(str(i-res))

print("Part 1: {}".format(mem[-1]))

