# Day 4.1
import re

ll = [x for x in open('input.txt').read().strip().split('\n')]

nums = ll[0]

boards = []
b = []

for l in range(2, len(ll)):
    if ll[l] == '':
        # New board
        print(b)
        boards.append(b)
        b = []
    else:
        row = []
        for num in re.split('\s+', ll[l].strip()):
            row.append(num)

        b.append(row)

# print("Part 1:", )


