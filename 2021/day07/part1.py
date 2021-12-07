import sys
from statistics import median

pos = [int(x) for x in sys.stdin.read().strip().split(',')]
target = int(median(pos))
print(median(pos))

dist = [abs(target - x) for x in pos]

print(sum(dist))