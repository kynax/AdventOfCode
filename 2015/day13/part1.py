import sys
import itertools

scores = {}
for line in sys.stdin:
	words = line.split()
	p = words[0]
	gl = words[2]
	g = int(words[3])
	o = words[10]
	o = o[0:-1]
	if not p in scores:
		scores[p] = {}
	scores[p][o] = g if gl == 'gain' else -g

best = 0
for perm in itertools.permutations(scores.keys()):
	total = 0
	for i in range(len(perm)):
		l = i-1
		r = i+1
		if r >= len(perm):
			r -= len(perm)
		total += scores[perm[i]][perm[l]] + scores[perm[i]][perm[r]]
	if total > best:
		best = total
		
print(best)