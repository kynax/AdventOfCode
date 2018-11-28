import sys

cp = []
global best, longest
best = 0
longest = 0

for l in sys.stdin:
	cp.append(list(int(c) for c in l.strip().split('/')))

def bridge(start, cps, score, length):
	found = False
	global best
	global longest

	for c in cps:
		if c[0] == start:
			found = True
			new_cps = cps.copy()
			new_cps.remove(c)
			bridge(c[1], new_cps, score + c[0] + c[1], length + 1)
			
		if c[1] == start:
			found = True
			new_cps = cps.copy()
			new_cps.remove(c)
			bridge(c[0], new_cps, score + c[0] + c[1], length + 1)
			
	if not found and score > best:
		print(score)
		best = score
		
	if not found and length >= longest:
		print(length, " long ", score, " strong")
		longest = length
		
bridge(0, cp, 0, 0)