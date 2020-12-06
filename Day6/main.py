# Day 6

file = open('input.txt')
lines = file.read().split("\n\n")


s = 0
for line in lines:
    letters = {}

    for l in line:
        for c in l.replace("\n", ""):
            letters[c] = 0

    s += len(letters.keys())


print(s)

