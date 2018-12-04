import sys 
from array import array

grid = array('h', (0 for i in range(0,1000 * 1000) ))
singles = []
duplicates = []

def print_grid():
	for i in range(1000):
		print(grid[i*1000:i*1000+1000])

def add(start, size, id):
	for x in range(int(start[0]), int(start[0]) + int(size[0])):
		for y in range(int(start[1]), int(start[1]) + int(size[1])):
			if grid[x + 1000 * y] == 0:
				if id not in singles and id not in duplicates:
					singles.append(id)
			else:
				if id in singles:
					singles.remove(id)
				if grid[x + 1000 * y] in singles:
					singles.remove(grid[x + 1000 * y])
				if id not in duplicates:
					duplicates.append(id)
				if grid[x + 1000 * y] not in duplicates:
					duplicates.append(grid[x + 1000 * y])
					
			grid[x + 1000 * y] = id

for l in sys.stdin:
	coords = l.strip().split(' @ ')[1].split(': ')
	start = coords[0].split(',')
	size = coords[1].split('x')
	id = int(l.strip().split(' @ ')[0][1:])
	
	add(start, size, id)

#print_grid()	
print('singles ', singles)