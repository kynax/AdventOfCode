def applymask(val, mask):
	val = list(val)
	for i in range(len(mask)):
		if mask[i] == 'X':
			continue
		val[i] = mask[i]
	return ''.join(val)

import sys

mem = {}
mask = ''
for l in sys.stdin:
	if l.startswith('mask'):
		mask = l.split(' = ')[1].strip()
		continue
	
	[adr, val] = l.split(' = ')
	bit = '{0:036b}'.format(int(val))
	val = applymask(bit, mask)
	mem[int(adr[4:-1])] = int(val,2)
	
#print(mem)
total = 0
for k,v in mem.items():
	total += v
	
print(total)