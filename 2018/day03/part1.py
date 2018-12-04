import sys 
from array import array

grid = array('h', (0 for i in range(0,1000 * 1000) ))

def print_grid():
	for i in range(1000):
		print(grid[i*1000:i*1000+1000])

def add(start, size):
	for x in range(int(start[0]), int(start[0]) + int(size[0])):
		for y in range(int(start[1]), int(start[1]) + int(size[1])):
			grid[x + 1000 * y] += 1

for l in sys.stdin:
	coords = l.strip().split(' @ ')[1].split(': ')
	start = coords[0].split(',')
	size = coords[1].split('x')
	
	add(start, size)

print_grid()	
print(1000 * 1000 - grid.count(0) - grid.count(1))