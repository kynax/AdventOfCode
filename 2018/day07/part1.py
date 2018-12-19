import sys

steps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N', 'O','P','Q','R','S','T','U','V','W','X','Y','Z']

for l in sys.stdin:
	#print(steps)
	pre = l.split(' ')[1]
	step = l.split(' ')[7]
	#print(pre, '->', step)
	
	if len(steps) == 0:
		steps.append(pre)
		steps.append(step)
		continue
		
	if steps.index(pre) < steps.index(step):
		continue
	
	if step in steps:
		steps.remove(step)
		
	idx = 0
	if pre in steps:
		idx = steps.index(pre) + 1
		
	#print('insert', step, 'at', idx, 'but check for alpha')
	while idx < len(steps) and ord(steps[idx]) < ord(step):
		idx += 1
	
	#print('will insert at', idx)
	steps.insert(idx, step)
	#print(steps)
	#print()
	
print(''.join(steps))