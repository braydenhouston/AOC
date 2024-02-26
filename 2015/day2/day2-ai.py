import os

def calculate_wrapping_paper(dimensions):
    total_paper = 0
    for dimension in dimensions:
        l, w, h = map(int, dimension.split('x'))
        sides = [l*w, w*h, h*l]
        total_paper += 2*sum(sides) + min(sides)
    return total_paper


def calculate_ribbon_length(dimensions):
    ribbon_length = 0
    for dimension in dimensions:
        l, w, h = map(int, dimension.split('x'))
        sides = [l, w, h]
        sides.sort()
        ribbon_length += 2 * (sides[0] + sides[1])  # ribbon to wrap the present
        ribbon_length += l * w * h  # ribbon for the bow
    return ribbon_length

# example usage


dimensions = [x for x in open(os.path.join(os.path.dirname(__file__),'input.txt')).read().strip().split('\n')]
print(calculate_wrapping_paper(dimensions))  # prints 101

# example usage:
print(calculate_ribbon_length(dimensions))
