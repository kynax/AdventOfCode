import sys

c = [0 for x in range(13)]

for l in sys.stdin:
	n = l.strip()
	
	for i in range(len(n)):
		if n[i] == '0':
			c[i] = c[i] -1
			
		if n[i] == '1':
			c[i] = c[i] + 1
			
g = ''
s = ''
for x in c:
	if x > 0:
		g += '1'
		s += '0'
	if x < 0:
		g += '0'
		s += '1'
		
print(int(g, 2) * int(s, 2))

