import sys

total = 0

for l in sys.stdin:
	sign = 1 if l[0] == '+' else -1
	diff = int(l.strip()[1:])
	total += sign * diff
	
print(total)