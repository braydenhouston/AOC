
#input = "1,9,10,3,2,3,11,0,99,30,40,50"

with open('input') as f:
    input = f.readline()

input = input.split(",")

for i in range(0, len(input)):
    input[i] = int(input[i])

CINPUT = input

def runProgram(noun, verb):
     input = CINPUT.copy()  # Reset Memory
     i = 0
     # Restore to the "1202 program alarm" state
     input[1] = noun
     input[2] = verb

     while i < len(input):
          if input[i] == 1:
               #print("Addition")
               input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
               i += 4
          elif input[i] == 2:
               #print("Multi")
               input[input[i+3]] = input[input[i+1]] * input[input[i+2]]
               i += 4
          elif input[i] == 99:
               #print("STOP")
               break
          else:
               return 1
     print("noun ", noun, " verb: ", verb, " Result ", input[0])
     return input[0]


#print(runProgram(12, 2))

for noun in range(0, 100):
     for verb in range(0, 100):
          if runProgram(noun, verb) == 19690720:
               print("100 * noun + verb is ", 100 * noun + verb )
               exit()
          verb += 1
     noun += 1
