import sys

lines = [l.strip() for l in sys.stdin]

def count(lines, dx, dy):
	total = 0
	x = 0
	
	for y in range(0, len(lines), dy):
		
		l = lines[y].strip()
	
		if l[x % len(l) ] == '#':
			total += 1
		x += dx
	
	return total


print(count(lines, 1, 1) * count(lines, 3, 1) * count(lines, 5, 1) * count(lines, 7, 1) * count(lines, 1, 2))