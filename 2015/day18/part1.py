import sys

part2 = False

lights = {}  # contains all the lights in (x,y) -> 0,1  (0 off, 1 on)
next_lights = {}  # next iteration of the lights
size = 0  # size of the input grid

def num(l):
	global lights
	total = 0
	total += lights.get((l[0]-1, l[1]-1), 0)
	total += lights.get((l[0]-1, l[1]  ), 0)
	total += lights.get((l[0]-1, l[1]+1), 0)
	total += lights.get((l[0],   l[1]-1), 0)
	#total += lights.get((l[0],   l[1]  ), 0) # self
	total += lights.get((l[0],   l[1]+1), 0)
	total += lights.get((l[0]+1, l[1]-1), 0)
	total += lights.get((l[0]+1, l[1]  ), 0)
	total += lights.get((l[0]+1, l[1]+1), 0)
	return total
	
def step():
	global lights
	global next_lights
	for l in lights.keys():
		n = num(l)
		if lights[l] == 0 and n == 3:
			next_lights[l] = 1
		elif lights[l] == 1 and (n == 2 or n == 3):
			next_lights[l] = 1
		else:
			next_lights[l] = 0
	lights = next_lights.copy()
	
	#### part 2
	if part2:
		lights[(0,0)] = 1 
		lights[(0,size-1)] = 1 
		lights[(size-1,0)] = 1 
		lights[(size-1,size-1)] = 1 
	####
	
def display():
	for x in range(size):
		s = ""
		for y in range(size):
			if lights[(x,y)] == 1:
				s += '#'
			else:
				s += '.'
		print(s)
		
def display_total():
	for x in range(size):
		s = ""
		for y in range(size):
			s += str(num((x,y)))
		print(s)

line_num = 0
for line in sys.stdin:
	col_num = 0
	for c in line:
		lights[(line_num, col_num)] = 1 if c == '#' else 0
		col_num += 1
	size = col_num
	line_num += 1

for i in range(100):
	step()
print(sum(lights.values()))