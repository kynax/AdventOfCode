import sys

i = []
pc = 0
rs = { 'a' : 12, 'b' : 0, 'c' : 0, 'd' : 0 }

for l in sys.stdin:
	i.append(l)
	
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
		pc += rs[i[pc].split()[2]] if i[pc].split()[2] in 'abcd' else int(i[pc].split()[2])
		continue
	
	if 'cpy' in i[pc]:
		if i[pc].split()[1] in 'abcd':
			rs[i[pc].split()[2]] = rs[i[pc].split()[1]]
		else:
			rs[i[pc].split()[2]] = int(i[pc].split()[1])
		pc += 1
		continue
		
	if 'tgl' in i[pc]:
		t = i[pc].split()[1]
		if not isinstance(t, int):
			t = rs[t]			
		
		if t+pc < 0 or t+pc >= len(i):
			pc+=1
			continue
			
		s = i[pc+t].split()
		
		if len(s) == 2: # one argument instruction
			if 'inc' in s[0]:
				i[pc+t] = 'dec ' + s[1]
			else:
				i[pc+t] = 'inc ' + s[1]

		if len(s) == 3: # two argument instruction
			if 'jnz' in s[0]:
				i[pc+t] = 'cpy ' + s[1] + ' ' + s[2]
			else:
				i[pc+t] = 'jnz ' + s[1] + ' ' + s[2]
			
		pc += 1
		continue
	
		
print(rs)