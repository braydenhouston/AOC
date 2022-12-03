import os
from string import ascii_lowercase
from string import ascii_uppercase

lower = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 
upper = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=27)}
letters = {**lower, **upper}

prioty_sum = 0

from itertools import islice
with open(os.path.join(os.path.dirname(__file__),'input.txt')) as f:
    while True:
        next_n_lines = list(islice(f, 3))
        if not next_n_lines:
            break
        if len(next_n_lines) == 1:
            break
        badge = ''.join(set(next_n_lines[0].replace('\n','')).intersection(next_n_lines[1].replace('\n','')).intersection(next_n_lines[2].replace('\n','')))
    
        prioty_sum += int(letters[badge])
    
print("Part 2: {}".format(prioty_sum))

