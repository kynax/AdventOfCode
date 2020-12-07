import sys

max = 0
for l in sys.stdin:
	l = l.strip()
	l = l.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
	
	row = int(l[:7],2)
	col = int(l[7:],2)
	
	id = row * 8 + col
	
	if id > max:
		max = id
		
print(max)
																	 