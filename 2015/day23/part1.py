import sys

inst = []
a = 0
### part 2
a = 1
###
b = 0
pc = 0

for line in sys.stdin:
	inst.append(line)
	
while True:
	if pc == len(inst):
		break
		
	cur = inst[pc]
	print(cur)
	
	if "hlf" in cur:
		if cur[4] == 'a':
			a /= 2
		else:
			b /= 2
		pc += 1
	elif "tpl" in cur:
		if cur[4] == 'a':
			a *= 3
		else:
			b *= 3
		pc += 1
	elif "inc" in cur:
		if cur[4] == 'a':
			a += 1
		else:
			b += 1
		pc += 1
	elif "jmp" in cur:
		cur = cur[4:]
		print(cur)
		offset = int(cur)
		pc += offset
	elif "jie" in cur:
		if (cur[4] == 'a' and a % 2 == 0) or (cur[4] == 'b' and b % 2 == 0):
			cur = cur[7:]
			offset = int(cur)
			pc += offset
		else:
			pc += 1
	elif "jio" in cur:
		if (cur[4] == 'a' and a == 1) or (cur[4] == 'b' and b == 1):
			cur = cur[7:]
			offset = int(cur)
			pc += offset
		else:
			pc += 1
	
print("a:",a,"b:",b)
		