import sys

arrival = int(sys.stdin.readline())
buses = []
for n in sys.stdin.readline().split(','):
    if n == 'x':
        continue

    buses.append(int(n))

print(arrival, buses)

best = 99999
bus = 0
for b in buses:
    m = b - (arrival % b)
    if m < best:
        best = m
        bus = b

print(bus, best, bus * best)
