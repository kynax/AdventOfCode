import sys
from collections import Counter

grid = []
roots = []

def print_grid():
	for y in range(400):
		s = ""
		for x in range(400):
			s += grid[x + 400*y]
		print(s)
		
def closest(x,y):
	total = 0
	for r in roots:
		dist = abs(r[1] - x) + abs(r[2] - y)
		total += dist
	if total < 10000:
		grid[x + 400*y] = '#'

for i in range(400*400):
	grid.append(' ')

id = 'A'
for l in sys.stdin:
	c = l.strip().split(', ')
	roots.append((id, int(c[0]), int(c[1])))
	id = chr(ord(id) + 1)
	if id == '[':
		id = 'a'
		
for y in range(400):
	for x in range(400):
		closest(x,y)
	

counts = [ g[0] for g in grid ]
print(Counter(counts).most_common(25))	
print_grid()

	
