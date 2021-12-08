import sys

def get(defs, n):
	return [x for x in defs if len(x) == n]

def get_has_all_other(defs, n, other):
	for d in defs:
		if len(d) != n:
			continue
			
		if all(x in d for x in other):
			return d
		
def get_not_segment(defs, n, seg):
	for d in defs:
		if len(d) != n:
			continue
			
		if seg not in d:
			return d
		
total = 0
for l in sys.stdin:
	top = None
	bot = None
	mid = None
	tl = None
	tr = None
	bl = None
	br = None
	
	defs, display = l.strip().split(' | ')
	defs = [sorted(x) for x in defs.split(' ')]
	
	digits = [None, 
			  get(defs,2)[0], 
			  None,
			  None,
			  get(defs,4)[0],
			  None,
			  None,
			  get(defs,3)[0],
			  get(defs,7)[0],
			  None
			 ]
	
	defs.remove(digits[1])
	defs.remove(digits[4])
	defs.remove(digits[7])
	defs.remove(digits[8])
	
	digits[9] = get_has_all_other(defs, 6, digits[4])
	digits[3] = get_has_all_other(defs, 5, digits[7])
	
	defs.remove(digits[9])
	defs.remove(digits[3])
	
	top = [x for x in digits[7] if x not in digits[1]][0] # using 7 - 1 -> top
	bl = [x for x in digits[8] if x not in digits[9]][0] # using 8 - 9 -> bottom left
	
	digits[5] = get_not_segment(defs, 5, bl)
	defs.remove(digits[5])
		
	digits[2] = get(defs, 5)[0]
	defs.remove(digits[2])
	
	digits[6] = get_has_all_other(defs, 6, digits[5])
	defs.remove(digits[6])
	digits[0] = get(defs, 6)[0]
	defs.remove(digits[0])
	
	reading = ''
	for d in display.split(' '):
		reading += str(digits.index(sorted(d)))
		
	total += int(reading)
	
print(total)
	
"""
n = 6	n = 2	n = 5	n = 5	n = 4	n = 5	n = 6	n = 3	n = 7	n = 6
xxxx	...x	xxxx	xxxx	x..x	xxxx	xxxx	xxxx	xxxx	xxxx
x  x	.  x	.  x	.  x	x  x	x  .	x  .	.  x	x  x	x  x
x..x	...x	xxxx	xxxx	xxxx	xxxx	xxxx	...x	xxxx	xxxx
x  x	.  x	x  .	.  x	.  x	.  x	x  x	.  x	x  x	.  x
xxxx	...x	xxxx	xxxx	.  x	xxxx	xxxx	...x	xxxx	xxxx
		n = 2					n = 4					n = 3	n = 7
				n = 5	n = 5			n = 5							n = 6
				not 	all 7			not bl							all 4
"""