import sys

x = 0
d = 0
a = 0

for l in sys.stdin:
	c, n = l.strip().split(' ')
	n = int(n)
	
	if c == 'forward':
		x += n
		d += (a*n)
		
	if c == 'down':
		a += n
		
	if c == 'up':
		a -= n
		
print(x * d)
	