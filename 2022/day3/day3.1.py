import os
from collections import Counter
from string import ascii_lowercase
from string import ascii_uppercase

lower = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 
upper = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=27)}
letters = {**lower, **upper}

ll = [x for x in open(os.path.join(os.path.dirname(__file__),'input.txt')).read().strip().split('\n')]
prioty_sum = 0
for l in ll:
    res_first = l[0:len(l)//2]
    res_second = l[len(l)//2:]

    first_count = Counter(res_first)
    sec_count = Counter(res_second)

    inter = ''.join(set(first_count).intersection(sec_count))
    prioty_sum += int(letters[inter])
    
print("Part 1: {}".format(prioty_sum))
