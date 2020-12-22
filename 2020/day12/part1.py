import sys

dirs = ((1,0),(0,-1),(-1,0),(0,1))
curDir = 0
x = 0
y = 0

for l in sys.stdin:
	l = l.strip()
	if l[0] == 'N':
		y += int(l[1:])
	if l[0] == 'S':
		y -= int(l[1:])
	if l[0] == 'E':
		x += int(l[1:])
	if l[0] == 'W':
		x -= int(l[1:])
		
	if l[0] == 'F':
		x += int(l[1:]) * dirs[curDir][0]
		y += int(l[1:]) * dirs[curDir][1]
		
	if l[0] == 'R':
		curDir += int(l[1:]) // 90
		curDir = curDir % 4
		
	if l[0] == 'L':
		curDir -= int(l[1:]) // 90
		curDir = curDir % 4
		
print(abs(x) + abs(y))