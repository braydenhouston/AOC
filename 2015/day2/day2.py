import os

ll = [x for x in open(os.path.join(os.path.dirname(__file__),'input.txt')).read().strip().split('\n')]

total_wrap = 0
ribbon_total = 0
for x in ll:
    l,w,h = [int(x) for x in x.split('x')]
    sides = [l,w,h]
    sides.sort()

    # Wrap
    subtotal_wrap = ((2*l*w) + (2*w*h) + (2*h*l)) + (sides[0]*sides[1])
    total_wrap += subtotal_wrap

    # Ribbon
    ribbon_sub = ((sides[0]*2) + (sides[1]*2)) + (l*w*h)
    ribbon_total += ribbon_sub

    print('wSub: {} rSub: {}'.format(subtotal_wrap, subtotal_wrap))

print('Total Wrap: {} Ribbon Total: {}'.format(total_wrap, ribbon_total))

