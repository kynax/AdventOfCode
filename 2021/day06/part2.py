import sys

qts = [0 for x in range(10)]
for r in [int(x) for x in sys.stdin.read().strip().split(',')]:
	qts[r] += 1

for d in range(256):
	new_qts = [0 for x in range(10)]
	for q in range(10):
		if q == 0:
			new_qts[6] += qts[0]
			new_qts[8] += qts[0]
		else:
			new_qts[q-1] += qts[q]
	qts = new_qts
			
print(sum(qts))