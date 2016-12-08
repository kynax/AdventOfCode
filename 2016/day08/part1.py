import sys
from collections import deque

# example
#w = 7
#h = 3

# part 1
w = 50
h = 6

lcd = []

def printLcd(lcd):
	for i in range(len(lcd)):
		s = ''
		for j in range(len(lcd[i])):
			s += lcd[i][j] 
		print(s)
	print()

for i in range(h):
	lcd.append(deque(['.' for x in range(w)]))

for line in sys.stdin:

	if 'rect' in line:
		# draw a new rectangle
		(a,b) = line.split(' ')[1].split('x')
		for i in range(int(b)):
			for j in range(int(a)):
				lcd[i][j] = '#'
	
	if 'row' in line:
		# rotate row (deque.rotate(n))
		(r,b) = line.split('=')[1].split(' by ')
		lcd[int(r)].rotate(int(b))
	
	if 'column' in line:
		# rotate column (manually?)
		(c,b) = line.split('=')[1].split(' by ')
		(c,b) = (int(c), int(b))
		for i in range(int(b)):
			t = lcd[h-1][c]
			for x in range(h-1,0,-1):
				lcd[x][c] = lcd[x-1][c]
			lcd[0][c] = t
		
	printLcd(lcd)
	
t = 0
for i in range(h):
	t += lcd[i].count('#')
print(t)