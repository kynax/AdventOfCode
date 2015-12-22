x = 0
y = 0
houses = [(0,0)]
for c in input():
	if c == 'v':
		y = y -1
	if c == '^':
		y = y + 1
	if c == '<':
		x = x - 1
	if c == '>':
		x = x + 1
	houses.append((x,y))

print(len(set(houses)))