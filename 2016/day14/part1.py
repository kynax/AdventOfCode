import hashlib
import re

my = 'ngcjuoqr'
#my = 'abc'

r3 = re.compile(r'(.)\1{2,}')

idx = 0
matches = []

def md5(i):
	s = my + str(i)
	m = hashlib.md5()
	m.update(s.encode('utf-8'))
	return m.hexdigest()

while True:

	h = md5(idx)
	
	r3m = r3.search(h)

	if r3m:
		c = r3m.group(0) + r3m.group(0)[0:2]
		c = c[0:5]
		
		for i in range(idx+1, idx+1001):
			if c in md5(i):
				matches.append((c,idx))
				break
	idx += 1
	
	if idx > 999999 or len(matches) >= 64:
		break
		
print(len(matches), matches)
	