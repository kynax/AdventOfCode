floor = 0
pos = 0
for c in input():
	pos = pos + 1
	if c == '(':
		floor = floor + 1
	if c == ')':
		floor = floor - 1
	
	if floor == -1:
		break
		
print(pos)