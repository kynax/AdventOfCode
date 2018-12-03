import sys
from collections import Counter

total2 = 0
total3 = 0

for l in sys.stdin:
	s = list(l.strip())
	s.sort()
	
	c = Counter(s)
	
	if 2 in c.values():
		total2 += 1
	if 3 in c.values():
		total3 += 1
		
print(total2 * total3)