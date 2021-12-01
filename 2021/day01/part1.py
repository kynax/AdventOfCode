import sys

prev = 999999
total = 0
for l in sys.stdin:
	cur = int(l.strip())
	if cur > prev:
		total += 1
	prev = cur
	
print(total)