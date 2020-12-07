# Day 6

file = open('input.txt')
lines = file.read().split("\n\n")
file.close()

s = 0
for line in lines:
    letters = {}
    for l in line:
        for c in l.replace("\n", ""):
            letters[c] = 0
    s += len(letters.keys())
print("Part 1 {}".format(s))


s = 0
for groups in lines:
    letters = {}
    person = groups.split("\n")
    for answers in person:
        for answer in answers:
            letters[answer] = letters.get(answer, 0) + 1
    for a in letters.keys():
        if letters[a] == len(person):
            s += 1
print("Part 2: {}".format(s))

