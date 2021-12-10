import sys

def score(l):
	total = 0
	for c in l:
		total = total * 5
		total += ' ([{<'.find(c)
	return total

incompletes = []
for l in sys.stdin:
	l = l.strip()
	
	good = True
	s = []
	for c in l:
		if c in '(<[{':
			s.append(c)
			continue
			
		if c == ')':
			o = s.pop()
			if o != '(':
				good = False
				break
		
		if c == ']':
			o = s.pop()
			if o != '[':
				good = False
				break
				
		if c == '}':
			o = s.pop()
			if o != '{':
				good = False
				break
				
		if c == '>':
			o = s.pop()
			if o != '<':
				good = False
				break
	if good:
		incompletes.append(''.join(s)[::-1])
		
scores = sorted(score(l) for l in incompletes)
print(scores[len(scores) // 2])
	