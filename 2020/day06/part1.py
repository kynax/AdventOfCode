import sys

total = 0
group = []
for l in sys.stdin:
	l = l.strip()
	if len(l) == 0:
		total += len(group)
		group = []
		continue
		
	for c in l:
		if c not in group:
			group.append(c)
			
print(total)