# Day 13.2
from itertools import count

file = open('input.txt')
payload = file.read().split("\n")
file.close()

timestamp, buses = [l.strip() for l in payload]
buses = sorted([(int(bus), idx) for idx, bus in enumerate(buses.split(',')) if bus != 'x'], reverse=True)

t, step = 0, 1
for bus, offs in buses:
    for c in count(t, step):
        if (c + offs) % bus == 0:
            t, step = c, step * bus
            break

print('part 2: %d' % t)

