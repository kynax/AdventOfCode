import sys

grid = [[0 for x in range(1000)] for x in range(1000)] 

for instruction in sys.stdin:
	sc = (0,0)
	ec = (0,0)
	i  = '-'
	s = ""
	if instruction.startswith("toggle "):
		i = 't'
		s = instruction[7:]
	if instruction.startswith("turn off "):
		i = 'f'
		s = instruction[9:]
	if instruction.startswith("turn on "):
		i = 'o'
		s = instruction[8:]
	coords = s.split(" through ")
	c = coords[0].split(",")
	sc = (int(c[0]), int(c[1]))
	c = coords[1].split(",")
	ec = (int(c[0]), int(c[1]))
	
	for x in range(sc[0], ec[0]+1):
		for y in range(sc[1], ec[1]+1):
			if i == 't':
				grid[x][y] = grid[x][y] + 2
			if i == 'o':
				grid[x][y] = grid[x][y] + 1
			if i == 'f':
				grid[x][y] = max(grid[x][y] - 1, 0)

total = 0				
for i in grid:
	for j in i:
		if j:
			total += j
print(total)