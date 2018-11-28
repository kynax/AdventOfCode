import sys

# read compressed text in
c = ''
for l in sys.stdin:
	c += l
	
i = 0
o = ''
while i < len(c):
	
	# if normal text, copy current char and continue
	if c[i] != '(':
		o += c[i]
		i += 1
		continue
	
	# start of a marker
	s = i+1 
	
	# find end of marker
	e = c[s:].index(')')
	
	# marker
	m = c[s:s+e]	
	l = int(m.split('x')[0])
	n = int(m.split('x')[1])
	
	print(l, n)
	
	# string to repeat
	t = c[s+e+1:s+e+l+1]
	
	print(t)
	
	# output the repetition
	for z in range(n):
		o += t
	i += e+l+2
	
	
print(o)
print(len(o))