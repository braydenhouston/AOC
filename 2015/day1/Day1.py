import os

ll = [x for x in open(os.path.join(os.path.dirname(__file__),'input.txt')).read().strip()]

FLOOR = 0
POS = 1

for x in ll:
    if x == '(':
        FLOOR += 1

    elif x == ')':
        FLOOR -= 1

    if FLOOR < 0:
        print('POS: {}'.format(POS))
        break

    POS += 1

# print('Floor: {}'.format(FLOOR))
    

    