import sys

bursts = 10000000

dirs = [ (0,1), (1,0), (0,-1), (-1,0) ]
cur_dir = 0
pos_x = 0
pos_y = 0

grid = {}

total = 0

for l in sys.stdin:
	pos_x = 0
	for c in l.strip():
		grid[(pos_x,pos_y)] = c
		pos_x += 1
	pos_y -= 1
	
pos_y = -12
pos_x = 12

#print(grid)
#print(pos_x, pos_y)

for i in range(bursts):
	
	# check if out of known bounds
	if (pos_x, pos_y) not in grid:
		grid[(pos_x,pos_y)] = '.'
	
	# next square
	if grid[(pos_x,pos_y)] == '.':
		cur_dir -= 1
	elif grid[(pos_x,pos_y)] == 'W':
		pass
	elif grid[(pos_x,pos_y)] == '#':
		cur_dir += 1
	elif grid[(pos_x,pos_y)] == 'F':
		cur_dir += 2	
	
	# change current
	if grid[(pos_x,pos_y)] == '.':
		grid[(pos_x,pos_y)] = 'W'
	elif grid[(pos_x,pos_y)] == 'W':
		grid[(pos_x,pos_y)] = '#'
		total += 1
	elif grid[(pos_x,pos_y)] == '#':
		grid[(pos_x,pos_y)] = 'F'
	elif grid[(pos_x,pos_y)] == 'F':
		grid[(pos_x,pos_y)] = '.'
		
	# move
	pos_x += dirs[cur_dir%4][0]
	pos_y += dirs[cur_dir%4][1]
	
print(total)
