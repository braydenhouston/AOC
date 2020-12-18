# Day 17.1

from collections import defaultdict

file = open('input.txt')

what = set()
for y, line in enumerate(file.read().splitlines(keepends=False)):
    for x, char in enumerate(line):
        if char == '#':
            what.add((x, y, ))


def p1(arg):
    neighborsΔ = set(
        (x, y, z,)
        for x in (-1, 0, 1,)
        for y in (-1, 0, 1,)
        for z in (-1, 0, 1,)
    )
    neighborsΔ.remove((0, 0, 0,))
    neighborsΔ = tuple(neighborsΔ)

    def tick(active_cubes):
        neighbors = defaultdict(int)
        for active_cube in active_cubes:
            for neighborΔ in neighborsΔ:
                neighbor = (
                    active_cube[0] + neighborΔ[0],
                    active_cube[1] + neighborΔ[1],
                    active_cube[2] + neighborΔ[2],
                )
                neighbors[neighbor] += 1

        for cube, active_neighbors_count in neighbors.items():
            if active_neighbors_count == 3:
                yield cube
            elif active_neighbors_count == 2:
                if cube in active_cubes:
                    yield cube

    state = set(
        (x, y, 0,)
        for x, y in arg
    )
    for _ in range(6):
        state = set(tick(state))
    return len(state)


def p2(arg):
    neighborsΔ = set(
        (x, y, z, w,)
        for x in (-1, 0, 1,)
        for y in (-1, 0, 1,)
        for z in (-1, 0, 1,)
        for w in (-1, 0, 1,)
    )
    neighborsΔ.remove((0, 0, 0, 0,))
    neighborsΔ = tuple(neighborsΔ)

    def tick(active_cubes):
        neighbors = defaultdict(int)
        for active_cube in active_cubes:
            for neighborΔ in neighborsΔ:
                neighbor = (
                    active_cube[0] + neighborΔ[0],
                    active_cube[1] + neighborΔ[1],
                    active_cube[2] + neighborΔ[2],
                    active_cube[3] + neighborΔ[3],
                )
                neighbors[neighbor] += 1

        for cube, active_neighbors_count in neighbors.items():
            if active_neighbors_count == 3:
                yield cube
            elif active_neighbors_count == 2:
                if cube in active_cubes:
                    yield cube

    state = set(
        (x, y, 0, 0,)
        for x, y in arg
    )
    for _ in range(6):
        state = set(tick(state))
    return len(state)


print(f'''part 1: {p1(what)}''')
print(f'''part 2: {p2(what)}''')
