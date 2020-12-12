import sys

d = []
length = 25

for l in sys.stdin:
	n = int(l.strip())
	d.append(n)
	
for i in range(len(d)):
	preamble = d[i:i+length]
	
	found = False
	for x in range(length):
		for y in range(length):
			if x == y:
				continue
				
			if preamble[x] + preamble[y] == d[i+length]:
				found = True
	
	if not found:
		print(d[i+length])
		break