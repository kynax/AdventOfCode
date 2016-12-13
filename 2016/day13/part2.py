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
			maze[i][j] = '###'
		else:
			maze[i][j] = '   '
			
maze[1][1] = 0

for step in range(50):
	for i in range(w-1):
		for j in range(h-1):
			
			# skip if done
			if isinstance(maze[i][j],int):
				continue
			
			# skip if wall
			if '#' in maze[i][j]:
				continue
			
			# find number of steps of adjacent squares
			u = maze[i][j-1] if isinstance(maze[i][j-1], int) else 99999
			d = maze[i][j+1] if isinstance(maze[i][j+1], int) else 99999
			l = maze[i-1][j] if isinstance(maze[i-1][j], int) else 99999
			r = maze[i+1][j] if isinstance(maze[i+1][j], int) else 99999
			
			# get the shortest one
			best = min(u,d,l,r)
			
			# if there was a way there, add one step to it
			if best != 99999 and best < 50:
				maze[i][j] = best+1

total = 0
for j in range(h):
	for i in range(w):
		if isinstance(maze[i][j], int):
			total += 1
print("Reachable in 50 steps : ", total)
				
for j in range(h):
	print('|'.join(str(x).zfill(3) for x in maze[j]))
	
