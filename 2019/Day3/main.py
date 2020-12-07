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
#wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
#wire2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")

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

print("Finding intersection of paths")

intercept = intersection(path1, path2)

shortDist = 0
shortcord = []
shortSteps = 0
fastcord = []

print("Finding shortest distance coords")
for cord in intercept:
     s = calcDistance(cord)
     if  s < shortDist or shortDist == 0:
          shortDist = s
          shortcord = cord

print("Finding fastest coords")
for cord in intercept:
     s = path1.index(cord) + path2.index(cord) + 2 # +2 to account for both lists 0 index
     if s < shortSteps or shortSteps == 0:
          shortSteps = s
          fastcord = cord

print("Shortest distance of ", shortDist, " is at ", shortcord)
print("Fastest in ", shortSteps, " steps is at ", fastcord)
