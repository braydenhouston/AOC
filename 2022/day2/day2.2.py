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
    op = key[op]
    me = key[me]

    # Find Move
    # Lose
    if me == 'R':
        if op == 'R': 
            me = 'S'
        elif op == 'P':
            me = 'R'
        elif op == 'S':
            me = 'P'
    # Tie
    elif me == 'P':
        me = op
    # Win
    elif me == 'S':
        if op == 'R': 
            me = 'P'
        elif op == 'P':
            me = 'S'
        elif op == 'S':
            me = 'R'
    
    # Shape
    if me == 'R':
        round_score += 1
    elif me == 'P':
        round_score += 2
    elif me == 'S':
        round_score += 3

    # Win
    if (me == 'R' and op == 'S') or (me == 'S' and op == 'P') or (me == 'P' and op == 'R'):
        round_score += 6
    # Tie
    if me == op:
        round_score += 3

    total_score += round_score

print(f"Part 2: {total_score}")