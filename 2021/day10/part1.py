import sys

total = 0
for l in sys.stdin:
	l = l.strip()
	
	s = []
	for c in l:
		if c in '(<[{':
			s.append(c)
			continue
			
		if c == ')':
			o = s.pop()
			if o != '(':
				total += 3
				break
		
		if c == ']':
			o = s.pop()
			if o != '[':
				total += 57
				break
				
		if c == '}':
			o = s.pop()
			if o != '{':
				total += 1197
				break
				
		if c == '>':
			o = s.pop()
			if o != '<':
				total += 25137
				break
		
print(total)