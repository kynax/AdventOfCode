import sys
import itertools

bucket = []
sols = []

for i in sys.stdin:
	bucket.append(int(i))
maxw = int(sum(bucket) / 4)
best = 99999999999
for i in range(len(bucket)):
	print(i)
	for c in itertools.combinations(bucket,i):
		if sum(c) == maxw:
			print(c)
			qe = 1
			for w in c:
				qe *= w
			if qe < best:
				best = qe
	if best < 99999999999:
		break
print(best)