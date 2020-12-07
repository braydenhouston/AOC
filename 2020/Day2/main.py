import re
with open('input.txt') as f:
    lines = f.readlines()

valid1 = 0
valid2 = 0
regex = r"(?P<min>\d+)-(?P<max>\d+)\s(?P<letter>\w):\s(?P<password>\w+)"
for line in lines:
    matches = re.search(regex, line)
    mn = int(matches.group("min"))
    mx = int(matches.group("max"))
    letter = matches.group("letter")
    password = matches.group("password")

    if mn <= password.count(letter) <= mx:
        valid1 += 1

    if (password[mn-1] == letter and password[mx-1] != letter) or \
       (password[mn-1] != letter and password[mx-1] == letter):
        valid2 += 1

print("Part 1: {}".format(valid1))
print("Part 2: {}".format(valid2))


