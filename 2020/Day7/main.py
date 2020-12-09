# Day 7

def can_contain(parent, child):
    if len(rules[parent]) == 0:
        return False
    elif child in [t for c, t in rules[parent]]:
        return True

    return any(can_contain(v, child) for c, v in rules[parent])


def contains(parent):
    children = 0
    for num, child in rules[parent]:
        children = children + (num * contains(child))
    return children + 1  # Count parent


file = open('input.txt')
bags = file.read().split("\n")
file.close()

rules = {}
for bag in bags:
    bagline = bag.replace(",", "").replace(".", "").split(" ")
    topbag = bagline[0] + bagline[1]

    sbags = []
    for i in range(4, len(bagline)-1, 4):
        if bagline[i] == "no":
            break
        sbag = bagline[i+1] + bagline[i+2]
        sbags.append((int(bagline[i]), sbag))

    rules[topbag] = sbags


print("Part 1: {}".format(sum(can_contain(bag, "shinygold") for bag in rules.keys())))
print("Part 2: {}".format(contains("shinygold") - 1))
