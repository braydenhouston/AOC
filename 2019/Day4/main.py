from itertools import groupby

min = 356261
max = 846303
count = 0
numbers = []   

for i in range(min, max+1):
     good = False
     numStr = str(i)

     # Test for double numbers
     for j in range(len(numStr) - 1):
          if numStr[j] == numStr[j + 1]:
               good = True
               break

     if not good:
          continue

     # Test for increase numbers
     for j in range(len(numStr) - 1):
          if(numStr[j] > numStr[j + 1]):
               good = False
               break

     if not good:
          continue

     numbers.append(numStr)
     count += 1

print("Total passwords: ", count) # Part 1

count = 0
for i in numbers:
     groups = groupby(i)
     result = [(label, sum(1 for _ in group)) for label, group in groups]

     for j in result:
          if j[1] == 2:
               count += 1
               break

print("Reduced passwords: ", count)  # Part 2
