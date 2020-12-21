import sys
from copy import deepcopy

grid = []
for l in sys.stdin:
	grid.append([c for c in l.strip()])
	
again = True
while again:
	new = deepcopy(grid)
	again = False
	for r in range(len(grid)):
		for c in range(len(grid[r])):
			occ = 0
			if r-1 >= 0 and c-1 >= 0 and grid[r-1][c-1] == '#':
				occ += 1
			if r-1 >= 0 and c >= 0 and grid[r-1][c] == '#':
				occ += 1
			if r-1 >= 0 and c+1 < len(grid[r]) and grid[r-1][c+1] == '#':
				occ += 1
			if r >= 0 and c-1 >= 0 and grid[r][c-1] == '#':
				occ += 1
			if r >= 0 and c+1 < len(grid[r]) and grid[r][c+1] == '#':
				occ += 1
			if r+1 < len(grid) and c-1 >= 0 and grid[r+1][c-1] == '#':
				occ += 1
			if r+1 < len(grid) and c >= 0 and grid[r+1][c] == '#':
				occ += 1
			if r+1 < len(grid) and c+1 < len(grid[r]) and grid[r+1][c+1] == '#':
				occ += 1

			if grid[r][c] == 'L' and occ == 0:
				new[r][c] = '#'
				again = True
			if grid[r][c] == '#' and occ >= 4:
				new[r][c] = 'L'
				again = True
			
	grid = new
		
			
			

total = 0
for r in grid:
	for c in r:
		if c == '#':
			total += 1
print(total)