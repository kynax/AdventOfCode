import sys

grid = {}

for l in sys.stdin:
	c1,c2 = l.strip().split(' -> ')
	x1,y1 = [int(c) for c in c1.split(',')]
	x2,y2 = [int(c) for c in c2.split(',')]
	
	if x1 == x2:
		if y1 > y2:
			y2,y1 = y1,y2
		for y in range(y1,y2+1):
			if (x1,y) not in grid:
				grid[(x1,y)] = 0
			grid[(x1,y)] = grid[(x1,y)] + 1
	if y1 == y2:
		if x1 > x2:
			x2,x1 = x1,x2
		for x in range(x1,x2+1):
			if (x,y1) not in grid:
				grid[(x,y1)] = 0
			grid[(x,y1)] = grid[(x,y1)] + 1
			
print(len([x for x in grid.values() if x > 1]))