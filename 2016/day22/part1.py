import sys

avail = []
data = []

for l in sys.stdin:
	if 'root' in l:
		continue
	if 'Avail' in l:
		continue
		
	s = l.split()
	name = s[0]
	n = name.split('-')
	x = n[1][1:]
	y = n[2][1:]
	size = int(s[1][:-1])
	used = int(s[2][:-1])
	avai = int(s[3][:-1])
	
	avail.append(avai)
	if used != 0:
		data.append(used)
	
avail.sort()
print(avail)

total = 0
for d in data:
	for i in range(len(avail)):
		if d < avail[i]:
			
			t = len(avail) - i
			print("Looking for nodes that can fit", d, " found",t)
			total += t
			break

print(total)