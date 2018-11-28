import sys

i = []
for l in sys.stdin:
	i.append(l)
	

def go(seed, i):
	pc = 0
	rs = { 'a' : seed, 'b' : 0, 'c' : 0, 'd' : 0 }
	out = ''
		
	while True:

		if pc > len(i)-1:
			break
		
		#print(i[pc])
		
		if 'inc' in i[pc]:
			rs[i[pc].split()[1]] += 1
			pc += 1
			continue
			
		if 'dec' in i[pc]:
			rs[i[pc].split()[1]] -= 1		
			pc += 1
			continue
		
		if 'jnz' in i[pc]:
			t = 0
			if i[pc].split()[1] in 'abcd':
				t = rs[i[pc].split()[1]]
			else:
				t = int(i[pc].split()[1])
			
			if t == 0:
				pc += 1
				continue
			pc += int(i[pc].split()[2])
			continue
		
		if 'cpy' in i[pc]:
			if i[pc].split()[1] in 'abcd':
				rs[i[pc].split()[2]] = rs[i[pc].split()[1]]
			else:
				rs[i[pc].split()[2]] = int(i[pc].split()[1])
			pc += 1
			continue
		if 'out' in i[pc]:
			if i[pc].split()[1] in 'abcd':
				out += str(rs[i[pc].split()[1]])
			else:
				out += str(int(i[pc].split()[1]))
			#print(out)
			pc += 1
			
			
		if len(out) == len('0101010101010101'):
			if out != '0101010101010101':
				print("Failed! with seed", seed)
				return False
			else:
				print("Success with seed", seed, "->", out)
				return True

for s in range(1000):
	if go(s,i):
		break