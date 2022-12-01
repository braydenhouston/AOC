import os

ll = [x for x in open(os.path.join(os.path.dirname(__file__),'input.txt')).read().strip().split('\n')]
cals = [0]
elf = 0

for l in ll: 
    if l == '':
        # print("New Elf")
        cals.append(0)
        continue
    else:
        cals[-1] += int(l)

cals.sort()
print(f"Part 1: {cals[-1]}")
print(f"Part 2: {sum(cals[-3::])}")