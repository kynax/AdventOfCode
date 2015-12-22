sx = 0
sy = 0
rx = 0
ry = 0
s = True
houses = [(0,0)]
for c in input():
	if s:
		if c == 'v':
			sy = sy - 1
		if c == '^':
			sy = sy + 1
		if c == '<':
			sx = sx - 1
		if c == '>':
			sx = sx + 1
		houses.append((sx,sy))
		s = False
	else:
		if c == 'v':
			ry = ry - 1
		if c == '^':
			ry = ry + 1
		if c == '<':
			rx = rx - 1
		if c == '>':
			rx = rx + 1
		houses.append((rx,ry))
		s = True

print(len(set(houses)))