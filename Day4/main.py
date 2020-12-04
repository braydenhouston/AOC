# Day 4

import re

with open('input.txt') as f:
    lines = f.readlines()

regex = r"^$"
pid = 0
passports = [{}]
temp = {}

for pos, line in enumerate(lines, start=0):
    if re.search(regex, line):
        pid += 1
        passports.append({})
        temp = {}
        continue

    for i in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]:
        matches = re.search(r"{}:(?P<field>[\w#]+)".format(i), line.strip())
        if matches:
            # print("Found {}: {}".format(i, matches.group("field")))
            temp[i] = matches.group("field")

    passports[pid] = {**temp, **passports[pid]}

valid = 0
for p in passports:
    if "byr" in p.keys() and "iyr" in p.keys() and "eyr" in p.keys() and "hgt" in p.keys() and \
       "hcl" in p.keys() and "ecl" in p.keys() and "pid" in p.keys():
        valid += 1
        continue

print("Part 1: {} valid".format(valid))
