import sys

x = 0
y = 0
sol = None
d = 'N'
T = {'L' : {'N' : 'W', 
			'W' : 'S', 
			'S' : 'E',
			'E' : 'N'}, 
	 'R' : {'N' : 'E',
	        'E' : 'S',
			'S' : 'W',
			'W' : 'N'} }
locations = []

steps = input()
#steps = 'R8, R4, R4, R8'
steps += ','
	
for step in steps.split():
	locations.append((x,y))
	#print(locations)
	t = step[0]
	d = T[t][d]
	c = int(step[1:-1])
	#print(d, step[1:-1]);
	while c > 0:
		if d == 'N':
			y += 1
		if d == 'S':
			y -= 1
		if d == 'E':
			x += 1
		if d == 'W':
			x -= 1
		if (x,y) in locations:
			sol = (x,y)
			break
		locations.append((x,y))
		c -= 1
	if sol != None:
		break

print('x :', x, ' y:', y)
print(abs(x) + abs(y))