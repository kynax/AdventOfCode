import sys

total = 0
group = None
for l in sys.stdin:
	l = l.strip()
	if len(l) == 0:
		print(group)
		total += len(group)
		group = None
		continue
		
	if group is None:
		group = set(l)
	else:
		group = group & set(l)
			
print(total)