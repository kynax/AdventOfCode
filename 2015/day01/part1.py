floor = 0
for c in input():
	if c == '(':
		floor = floor + 1
	if c == ')':
		floor = floor - 1
		
print(floor)