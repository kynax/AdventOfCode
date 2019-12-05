import sys

t = [int(l.strip()) // 3 - 2 for l in sys.stdin]
print(sum(t))