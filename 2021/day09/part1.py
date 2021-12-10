import sys

def ns(x,y):
	n = []
	n.append((x+1,y))
	if x > 0:
		n.append((x-1,y))
	n.append((x,y+1))
	if y > 0:
		n.append((x,y-1))
	return n

grid = []

for l in sys.stdin:
	grid.append([int(x) for x in l.strip()])
	
total = 0
for y in range(len(grid)):
	for x in range(len(grid[y])):
		total += grid[y][x]+1
		for nx,ny in ns(x,y):
			if ny >= len(grid) or nx >= len(grid[y]):
				continue
			if grid[y][x] >= grid[ny][nx]:
				total -= grid[y][x]+1
				break
			
print(total)