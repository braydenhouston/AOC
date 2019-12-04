min = 356261
max = 846303
count = 0

for i in range(min, max+1):
     good = False
     numStr = str(i)

     # Test for double numbers
     for j in range(len(numStr) - 1):
          if numStr[j] == numStr[j + 1]:
               good = True
               break

     if not good:
          #print(i, " doesn't only increase")
          continue

     # Test for increase numbers
     for j in range(len(numStr) - 1):
          if(numStr[j] > numStr[j + 1]):
               good = False
               break

     if not good:
          #print(i, " doesn't only increase")
          continue

     count += 1

print("Total passwords: ", count)
