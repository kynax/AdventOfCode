import sys
import itertools

e = [int(l) for l in sys.stdin]

for i in e:
	for j in e:
		if i == j:
			continue
		if i + j == 2020:
			print(i * j)
			exit()