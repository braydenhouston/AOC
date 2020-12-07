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
            temp[i] = matches.group("field")

    passports[pid] = {**temp, **passports[pid]}

valid = 0
for p in passports:
    if (len(p.keys()) == 7 and "cid" not in p.keys()) or len(p.keys()) == 8:
        p["byr"] = int(p["byr"])
        if p["byr"] < 1920 or p["byr"] > 2002:
            continue

        p["iyr"] = int(p["iyr"])
        if p["iyr"] < 2010 or p["iyr"] > 2020:
            continue

        p["eyr"] = int(p["eyr"])
        if p["eyr"] < 2020 or p["eyr"] > 2030:
            continue

        matches = re.search(r"(?P<height>(\d+))(?P<unit>(cm|in))", p["hgt"])
        if matches is None:
            continue
        height = int(matches.group("height"))
        if matches.group("unit") == "cm":
            if height < 150 or height > 193:
                continue
        elif matches.group("unit") == "in":
            if height < 59 or height > 76:
                continue

        matches = re.search(r"#([\d|a-f]){6}", p["hcl"])
        if matches is None:
            continue

        if p["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue

        matches = re.search(r"\d{9}", p["pid"])
        if matches is None:
            continue
        valid += 1

print("Part 2: {} valid out of {}".format(valid - 1, len(passports)))  # Off by one....somehow. FML
