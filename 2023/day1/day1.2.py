import re
import os

sum = 0
lookups = ["[0-9]", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open(os.path.join(os.path.dirname(__file__),'input.txt')) as input:
    while line := input.readline():
        numbers = re.findall(f"(?=({'|'.join(lookups)}))", line)
        first   = numbers[0]                if numbers[0].isdigit()                else lookups.index(numbers[0])
        last  = numbers[len(numbers) - 1] if numbers[len(numbers) - 1].isdigit() else lookups.index(numbers[len(numbers) - 1])
        print(f"{first}{last}")
        sum += int(f"{first}{last}")

print(sum)