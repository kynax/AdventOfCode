import sys

total = 0
for l in sys.stdin:
	defs, display = l.strip().split(' | ')
	
	total += sum([1 for x in display.split() if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7])
	
print(total)