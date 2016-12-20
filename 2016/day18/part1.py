my = '^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......'
#my = '.^^.^.^^^^'
nb = 40
total = 0

def isTrap(l,c,r):
	if l == '^' and c == '^' and r == '.':
		return True
	if l == '.' and c == '^' and r == '^':
		return True
	if l == '^' and c == '.' and r == '.':
		return True
	if l == '.' and c == '.' and r == '^':
		return True
	
	return False

#print(my)
total += my.count('.')
x = my
for i in range(nb-1):
	n = ''
	for i in range(len(x)):
		l = x[i-1] if i > 0 else '.'
		c = x[i]
		r = x[i+1] if i < len(x) -1 else '.'
		n += '^' if isTrap(l,c,r) else '.'
	#print(n)
	total += n.count('.')
	x = n
print(total)