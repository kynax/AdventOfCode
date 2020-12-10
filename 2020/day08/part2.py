import sys

c = []

for l in sys.stdin:
	c.append(l)
	
pc = 0
acc = 0
result = None

for fix in range(len(c)):
	
	code = c.copy()
	
	if code[fix].startswith('acc'):
		continue
	
	if code[fix].startswith('nop'):
		code[fix] = code[fix].replace('nop','jmp')
	else:
		code[fix] = code[fix].replace('jmp','nop')
	
	pc = 0
	acc = 0
	while True:
		if len(code) == pc:
			result = acc
			break

		i = code[pc]

		if i[0] == 'x':
			break

		code[pc] = 'x' + code[pc]
		if i.startswith('acc'):
			acc += int(i[4:])
			pc += 1
		if i.startswith('nop'):
			pc += 1
		if i.startswith('jmp'):
			pc += int(i[4:])
	
	if result is not None:
		break
		
print(result)