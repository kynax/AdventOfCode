import sys

x = 0
y = 0
d = 'N'
T = {'L' : {'N' : 'W', 
			 'W' : 'S', 
			 'S' : 'E',
			 'E' : 'N'}, 
	 'R' : {'N' : 'E',
	         'E' : 'S',
			 'S' : 'W',
			 'W' : 'N'} }

steps = input()
steps += ','
for step in steps.split():
	t = step[0]
	d = T[t][d]
	c = int(step[1:-1])
	#print(d, step[1:-1]);
	if d == 'N':
		y += c
	if d == 'S':
		y -= c
	if d == 'E':
		x += c
	if d == 'W':
		x -= c

print('x :', x, ' y:', y)
print(abs(x) + abs(y))