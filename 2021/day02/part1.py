import sys

x = 0
d = 0
for l in sys.stdin:
	c, n = l.strip().split(' ')
	n = int(n)
	
	if c == 'forward':
		x += n
		
	if c == 'down':
		d += n
		
	if c == 'up':
		d -= n
		
print(x * d)
	