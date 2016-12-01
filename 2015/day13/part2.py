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
keys = list(scores.keys())
keys.append("Me")
for perm in itertools.permutations(keys):
	total = 0
	for i in range(len(perm)):
		l = i-1
		r = i+1
		if r >= len(perm):
			r -= len(perm)
		person = scores.get(perm[i], {})
		sl = person.get(perm[l], 0)
		sr = person.get(perm[r], 0)
		total += sl + sr
	if total > best:
		best = total
		
print(best)