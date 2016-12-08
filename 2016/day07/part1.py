import sys

t = 0
for l in sys.stdin:
	f = False
	b = False
	
	for i in range(len(l) - 3):
	
		if l[i] == '[':
			b = True
			continue
			
		if l[i] == ']':
			b = False
			continue
			
		if l[i] == l[i+3] and l[i+1] == l[i+2] and l[i] != l[i+1]:
			# found an ABBA, check if not between brackets
			if b:
				f = False
				break
			f = True
	if f:
		t+=1

print(t)