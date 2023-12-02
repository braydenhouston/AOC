import os

sum = 0

with open(os.path.join(os.path.dirname(__file__),'input.txt')) as input:
    while line := input.readline():
        game  = line.split(":")[0].split(" ")[1].strip()
        rounds = line.split(":")[1].strip().split(";")

        threshold = {
            "red":   12,
            "green": 13,
            "blue":  14
        }

        pulls = {
            "red":   0,
            "green": 0,
            "blue":  0
        }

        bad_game = False
        
        for moves in rounds:
            for move in moves.split(","):
                number, color = move.strip().split(" ")

                if int(number) > threshold[color]:
                    bad_game = True
                    break

        if not bad_game:
            sum += int(game)

    print("Total: {}".format(sum))

