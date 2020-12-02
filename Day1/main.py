from numpy import loadtxt
lines = loadtxt("Day1/input.txt", comments="#", delimiter="\n", unpack=False)


def part1():
    for pos, num in enumerate(lines, start=0):
        for spos, snum in enumerate(lines, start=pos+1):
            if num + snum == 2020:
                print("Part 1 Answer: {}".format(num * snum))
                return


def part2():
    for pos, num in enumerate(lines, start=0):
        for spos, snum in enumerate(lines, start=pos + 1):
            for tpos, tnum in enumerate(lines, start=pos + 2):
                if num + snum + tnum == 2020:
                    print("Part 2 Answer: {}".format(num * snum * tnum))
                    return


part1()
part2()
