import sys
from statistics import median

def cost(n,t):
	d = abs(t-n)+1
	return d*(d-1) // 2

def fuel(pos, t):
	return sum([cost(x,t) for x in pos])

pos = [int(x) for x in sys.stdin.read().strip().split(',')]
target = int(median(pos))

costs = [fuel(pos,x) for x in range(len(pos))]

print(min(costs))