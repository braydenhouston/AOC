# Day 5
import math

def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1)
            if x not in lst]


with open('input.txt') as f:
    lines = f.readlines()

seats = []
maxid = 0

for line in lines:
    lr, ur, lc, uc = 0, 127, 0, 7
    for l in line:
        if l == "F":
            ur -= math.ceil((ur-lr)/2) if ur - math.ceil((ur-lr)/2) != lr else 0
        elif l == "B":
            lr += math.ceil((ur-lr)/2) if lr + math.ceil((ur-lr)/2) != ur else 0
        elif l == "R":
            lc += math.ceil((uc - lc) / 2) if lc + math.ceil((uc-lc)/2) != uc else 0
        elif l == "L":
            uc -= math.ceil((uc - lc) / 2) if uc - math.ceil((uc-lc)/2) != lc else 0
        else:
            continue

    row = lr if line[6] == "F" else ur
    col = uc if line[9] == "R" else lc

    seatid = row * 8 + col
    seats.append(seatid)
    if seatid > maxid:
        maxid = seatid

seats.sort()

print("Part 1: {}".format(maxid))
print("Part 1: {}".format(find_missing(seats)))