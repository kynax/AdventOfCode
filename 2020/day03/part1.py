import sys

x = 0
total = 0
for l in sys.stdin:
	
	l = l.strip()
	
	if l[x % len(l) ] == '#':
		total += 1
	x += 3
	
print(total)