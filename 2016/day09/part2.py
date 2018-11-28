import sys

# read compressed text in
c = ''
for l in sys.stdin:
	c += l
	
dbg = 0
o = ''
total = 0
text = True
while '(' in c:
	i = 0
	o = ''
	print("Pass #", dbg, " compressed length:",len(c))
	text = True
	while i < len(c):
		
		# if normal text, copy current char and continue
		if c[i] != '(':
			if text:
				total += 1
			else:
				o += c[i]
				i += 1
			continue
		
		text = False
		# start of a marker
		s = i+1 
		
		# find end of marker
		e = c[s:].find(')')
		
		# marker
		m = c[s:s+e]	
		l = int(m.split('x')[0])
		n = int(m.split('x')[1])
		
		#print(l, n)
		
		# string to repeat
		t = c[s+e+1:s+e+l+1]
		
		#print(t)
		
		# output the repetition
		for z in range(n):
			o += t
		#print("After expansion :",o)
		i += e+l+2
	c = o
	#print(o)
	#print()
	dbg += 1
	
#print(o)
print(len(o))