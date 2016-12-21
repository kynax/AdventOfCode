import sys

#ps = list('abcde')
ps = list('abcdefgh')

def swapPos(s, x, y):
	print("swapPos", x, y)
	lx = s[x]
	ly = s[y]
	ns = s
	ns[x] = ly
	ns[y] = lx
	return ns

def swapLet(s, x, y):
	ix = s.index(x)
	iy = s.index(y)
	s[ix] = y
	s[iy] = x
	return s
	
def rotateLeft(s, x):
	return s[x:] + s[:x]
	
def rotateRight(s, x):
	return s[-x:] + s[:-x]
	
def rotatePos(s, x):
	n = s.index(x)
	if n >= 4:
		n += 1
	return rotateRight(s,(n+1) % len(s))
	
def reverse(s, x, y):
	ns = s[:x]
	ns.extend(s[x:y+1][::-1])
	ns.extend(s[y+1:])
	return ns
	
def move(s, x, y):
	l = s[x]
	ns = s[:x] + s[x+1:]
	ns.insert(y,l) 
	return ns
	
password = ps
for l in sys.stdin:
	if 'swap position' in l:
		splt = l.split()
		password = swapPos(password, int(splt[2]), int(splt[5]))
	
	if 'swap letter' in l:
		splt = l.split()
		password = swapLet(password, splt[2], splt[5])
	
	if 'reverse' in l:
		splt = l.split()
		password = reverse(password, int(splt[2]), int(splt[4]))
		
	if 'rotate left' in l:
		splt = l.split()
		password = rotateLeft(password, int(splt[2]))
		
	if 'rotate right' in l:
		splt = l.split()
		password = rotateRight(password, int(splt[2]))
		
	if 'move' in l:
		splt = l.split()
		password = move(password, int(splt[2]), int(splt[5]))
		
	if 'rotate based' in l:
		splt = l.split()
		password = rotatePos(password, splt[6])
		
	print(password)

print(''.join(password))