import sys

total = 0
diffs = []
freqs = []
dup = None

for l in sys.stdin:
	sign = 1 if l[0] == '+' else -1
	diff = int(l.strip()[1:])
	diffs.append(sign * diff)

i = 0
while dup is None:
	total += diffs[i% len(diffs)]
	if total in freqs:
		dup = total
	freqs.append(total)
	print(total)
	i += 1
	
print(dup)