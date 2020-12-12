import sys

target = 393911906
d = []

for l in sys.stdin:
	d.append(int(l.strip()))
			 
for s in range(len(d)):
	total = d[s]
	e = s + 1
	while total < target:
		total += d[e]
		e += 1
		if total == target:
			print(min(d[s:e]) + max(d[s:e]))
			exit()