import sys

global GRID_SIZE_X
global GRID_SIZE_Y

def ns(x,y):
	n = []
	if x < GRID_SIZE_X-1:
		n.append((x+1,y))
	if x > 0:
		n.append((x-1,y))
	if y < GRID_SIZE_Y-1:
		n.append((x,y+1))
	if y > 0:
		n.append((x,y-1))
	return n

def get_bassin(x,y):
	#print('get_bassin',x,y)
	m = 10
	bx = -1
	by = -1
	
	if (x,y) in bassins:
		return (x,y)
	
	for nx,ny in ns(x,y):
		if grid[ny][nx] < m:
			m = grid[ny][nx]
			bx = nx
			by = ny
	return get_bassin(bx,by)
	
	

global grid
grid = []

for l in sys.stdin:
	grid.append([int(x) for x in l.strip()])
GRID_SIZE_X = len(grid[0])
GRID_SIZE_Y = len(grid)

global bassins
bassins = {}
for y in range(len(grid)):
	for x in range(len(grid[y])):
		
		if grid[y][x] == 9:
			continue
			
		if all(grid[y][x] < grid[ny][nx] for nx,ny in ns(x,y)):
			if (x,y) not in bassins:
				bassins[(x,y)] = 0
			bassins[(x,y)] = bassins[(x,y)] + 1

for y in range(len(grid)):
	for x in range(len(grid[y])):
		
		if grid[y][x] == 9:
			continue
			
		if (x,y) not in bassins:
			#print('looking for', x,y, 'which has value', grid[y][x])
			bx,by = get_bassin(x,y)
			bassins[(bx,by)] = bassins[(bx,by)] + 1
			
			
sizes = sorted(v for k,v in bassins.items())
print(sizes[-1] * sizes[-2] * sizes[-3])