import sys

t = 0

for line in sys.stdin:
	l = [int(s) for s in line.split()]
	if sum(l) - max(l) > max(l):
		t += 1
		
print(t)