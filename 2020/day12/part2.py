import sys

rot = ((0,1),(-1,0),(0,-1),(1,0))

x = 0
y = 0
wpx = 10
wpy = 1

for l in sys.stdin:
	l = l.strip()
	if l[0] == 'N':
		wpy += int(l[1:])
	if l[0] == 'S':
		wpy -= int(l[1:])
	if l[0] == 'E':
		wpx += int(l[1:])
	if l[0] == 'W':
		wpx -= int(l[1:])
		
	if l[0] == 'F':
		x += int(l[1:]) * wpx
		y += int(l[1:]) * wpy
		
	if l[0] == 'R':
		r = rot[(int(l[1:]) // 90)-1]

		xnew = wpx * r[0] + wpy * r[1];
		ynew = -wpx * r[1] + wpy * r[0];
		
		wpx = xnew
		wpy = ynew
		
		
	if l[0] == 'L':
		r = rot[(int(l[1:]) // 90)-1]

		xnew = wpx * r[0] - wpy * r[1];
		ynew = wpx * r[1] + wpy * r[0];

		wpx = xnew
		wpy = ynew
		
print(abs(x) + abs(y))