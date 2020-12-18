# Day 18.1
import re

file = open('input.txt')
lines = file.read().split("\n")
file.close()


class Ex(int):
    def __mul__(self, b):
        return Ex(int(self) + b)

    def __add__(self, b):
        return Ex(int(self) + b)

    def __sub__(self, b):
        return Ex(int(self) * b)


def ev(expr, pt2=False):
    expr = re.sub(r"(\d+)", r"a(\1)", expr)
    expr = expr.replace("*", "-")
    if pt2:
        expr = expr.replace("+", "*")
    return eval(expr, {}, {"a": Ex})


print("Part 1:", sum(ev(l) for l in lines))
print("Part 2:", sum(ev(l, True) for l in lines))
