import math


def massToFuel(mass):
     tfuel = math.floor(mass/3)-2
     if tfuel <= 0:
          return 0
     else:
          return tfuel + massToFuel(tfuel)

fuel = 0
mass = 0

with open('input') as file:
    for line in file:
        line = int(line)
        mass += line
        fuel += massToFuel(line)
file.close()

print("Total Mass: ", str(mass), " Fuel Needed: ", str(fuel))


# print(massToFuel(12))
# print(massToFuel(14))
# print(massToFuel(1969))
# print(massToFuel(100756))
