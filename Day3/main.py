def updateCord(cord, dir):
     if dir == "U":
          cord[1] += 1
     elif dir == "D":
          cord[1] -= 1
     elif dir == "L":
          cord[0] -= 1
     elif dir == "R":
          cord[0] += 1
     return cord

def intersection(lst1, lst2):
    return [item for item in lst1 if item in lst2]

def calcDistance(cord):
     return abs(cord[0] - 0) + abs(cord[1] - 0)


f = open('input')
lines = f.readlines()
wire1 = lines[0].rstrip().split(",")
wire2 = lines[1].rstrip().split(",")

# Test Cases
# wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
# wire2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")

cords = [0, 0]

path1 = []
path2 = []  

print("Running path 1")
for dir in wire1:
     cmd = dir[:1]
     step = int(dir[1:])
     for i in range(step):
          path1.append(updateCord(cords, cmd)[:])

cords = [0, 0]

print("Running path 2")
for dir in wire2:
     cmd = dir[:1]
     step = int(dir[1:])
     for i in range(step):
          path2.append(updateCord(cords, cmd)[:])

print("Finding intersection")
intercept = intersection(path1, path2)

shortest = 0
shortcord = []

print("Finding distance")
for cord in intercept:
     s = calcDistance(cord)
     if  s < shortest or shortest == 0:
          shortest = s
          shortcord = cord

print("Shortest distance of ", shortest, " is at ", shortcord)
