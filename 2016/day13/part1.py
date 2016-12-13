my = 1352
h = 60
w = 60

maze = [[' ' for x in range(w)] for y in range(h)]

def isWall(x,y):
	f = x*x + 3*x + 2*x*y + y + y*y
	f += my
	b = bin(f)
	return b.count('1') % 2 == 1
	
for i in range(60):
	for j in range(60):
		if isWall(i,j):
			maze[i][j] = '#'
		else:
			maze[i][j] = ' '
			
maze[1][1] = 'S'
maze[31][39] = 'E'

for j in range(h):
	print(''.join(maze[j]))