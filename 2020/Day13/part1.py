# Day 13.1

file = open('input.txt')
payload = file.read().split("\n")
file.close()

time = int(payload[0])
times = {}
buses = []

for i in payload[1].split(","):
    if i == "x":
        continue
    buses.append(int(i))

for bus in buses:
    if (time - (time % bus)) + bus > time:
        times[bus] = (time - (time % bus)) + bus

waitid = min(times, key=times.get)
wait = times[waitid] - time

print("Part 1: {}".format(wait*waitid))
