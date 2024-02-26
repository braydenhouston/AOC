import os

total = 0
power_list = []

with open(os.path.join(os.path.dirname(__file__),'input.txt')) as input:
    while line := input.readline():
        game  = line.split(":")[0].split(" ")[1].strip()
        rounds = line.split(":")[1].strip().split(";")

        limits = {
            "red":   12,
            "green": 13,
            "blue":  14
        }

        mins = {
            "red":  0,
            "green":0,
            "blue": 0
        }

        bad_game = False
        
        for moves in rounds:
            for move in moves.split(","):
                number, color = move.strip().split(" ")
                number = int(number)

                if number > limits[color]:
                    bad_game = True

                if number > mins[color]:
                    mins[color] = number

        if not bad_game:
            total += int(game)
        
        power_list.append(  mins["red"] * mins["green"] * mins["blue"] )

    print("Part 1 Total: {}".format(total))
    print("Part 2 Power Total: {}".format(sum(power_list)))

