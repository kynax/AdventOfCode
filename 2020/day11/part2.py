import sys
from copy import deepcopy

grid = []
for l in sys.stdin:
	grid.append([c for c in l.strip()])
	
maxR = len(grid)
maxC = len(grid[0])
dirs = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
	
again = True
while again:
	new = deepcopy(grid)
	again = False
	for r in range(len(grid)):
		for c in range(len(grid[r])):

			occ = 0
			for d in dirs:
							
				x = r + d[0]
				y = c + d[1]
				while x >= 0 and y >= 0 and x < maxR and y < maxC:
					if grid[x][y] == '#':
						occ += 1
						break
					if grid[x][y] == 'L':
						break
					x += d[0]
					y += d[1]
				

			if grid[r][c] == 'L' and occ == 0:
				new[r][c] = '#'
				again = True
			if grid[r][c] == '#' and occ >= 5:
				new[r][c] = 'L'
				again = True
			
	grid = new
		
			
			

total = 0
for r in grid:
	for c in r:
		if c == '#':
			total += 1
print(total)