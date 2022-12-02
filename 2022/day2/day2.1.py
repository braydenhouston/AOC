import os

ll = [x for x in open(os.path.join(os.path.dirname(__file__),'input.txt')).read().strip().split('\n')]

total_score = 0 

key = {
    "A": "R",
    "B": "P",
    "C": "S",
    "X": "R",
    "Y": "P",
    "Z": "S",
}

for r in ll:
    round_score = 0
    op, me = r.split(" ")

    # Shape
    if me == 'X':
        round_score += 1
    elif me == 'Y':
        round_score += 2
    elif me == 'Z':
        round_score += 3

    # Win
    if (key[me] == 'R' and key[op] == 'S') or (key[me] == 'S' and key[op] == 'P') or (key[me] == 'P' and key[op] == 'R'):
        round_score += 6
    # Tie
    if key[me] == key[op]:
        round_score += 3

    total_score += round_score

print(f"Part 1: {total_score}")