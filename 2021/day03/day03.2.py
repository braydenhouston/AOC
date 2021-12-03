# Day 3.2

from collections import Counter

lines = [x for x in open('input.txt').read().strip().split('\n')]

gamma = ''
eps = ''


for i in range(len(lines[0])):
    common = Counter(x[i] for x in lines)

    if common['0'] > common['1']:
        lines = [ x for x in lines if x[i]== '0' ]
    else:
        lines = [ x for x in lines if x[i]== '1' ]
    gamma = lines[0]

lines = [x for x in open('input.txt').read().strip().split('\n')]

for i in range(len(lines[0])):
    common = Counter(x[i] for x in lines)

    if common['0'] > common['1']:
        lines = [ x for x in lines if x[i]== '1' ]
    else:
        lines = [ x for x in lines if x[i]== '0' ]
    if lines:
        eps = lines[0]

print("Part 2:", int(gamma,2) * int(eps,2) )
