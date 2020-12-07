import sys

seats = []
for l in sys.stdin:
	l = l.strip()
	l = l.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
	
	row = int(l[:7],2)
	col = int(l[7:],2)
	
	id = row * 8 + col
	
	seats.append(id)
		
seats.sort()

prev = 0
for s in seats:
	if s - prev != 1:
		print(prev, s)
	prev = s