import sys
import itertools

e = [int(l) for l in sys.stdin]

for i in e:
	for j in e:
		for k in e:
			if i == j or j == k or i == k:
				continue
			if i + j + k == 2020:
				print(i * j * k)
				exit()