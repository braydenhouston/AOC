# Day 9

file = open('input.txt')
payload = file.read().split("\n")
file.close()


def run(number, list):
    for x in list:
        x = int(x)
        for y in list:
            y = int(y)
            if x == y:
                continue
            if (x+y) == int(number):
                return True
    return False


weak = 0
for pos in range(25, len(payload)):
    if run(payload[pos], payload[pos-25:pos]) is False:
        weak = int(payload[pos])
        print("Part 1: {}".format(payload[pos]))
        break

s = 0
e = 1
while s <= len(payload):
    t = payload[s:e]
    t = list(map(int, t))
    if sum(t) > weak:
        s += 1
        e = s
    elif sum(t) == weak:
        t.sort()
        print("S: {} L: {} Sum: {}".format(t[0], t[-1], sum([t[0], t[-1]])))
        break
    e += 1
