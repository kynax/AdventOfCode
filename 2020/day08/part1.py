import sys

code = []

for l in sys.stdin:
	code.append(l)
	
pc = 0
acc = 0
while True:
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
		
print(acc)