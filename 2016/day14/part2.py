"""Solves http://adventofcode.com/2016/day/14"""

import hashlib
import re
from collections import deque

MY_INPUT = 'ngcjuoqr'
#MY_INPUT = 'abc'

RE3 = re.compile(r'(.)\1{2,}')

def md5(i):
	s = MY_INPUT + str(i)
	for i in range(2017):
		m = hashlib.md5()
		m.update(s.encode('utf-8'))
		s = m.hexdigest()
	return s

idx = 0
matches = []
print("Initialize list of next 1000 hashes.")
nextmd5 = deque(md5(i) for i in range(1000))
print("Done.")

print("Start searching...")
while True:
	nextmd5.popleft()
	nextmd5.append(md5(idx+1000))
	
	h = md5(idx)
	r3m = RE3.search(h)

	if r3m:
		c = r3m.group(0) + r3m.group(0)[0:2]
		c = c[0:5]
		
		for m in nextmd5:
			if c in m:
				matches.append((c,idx))
				break
	idx += 1
	
	if idx % 1000 == 0:
		print(idx)

	if idx > 999999 or len(matches) >= 64:
		break
		
print(len(matches), matches)
	