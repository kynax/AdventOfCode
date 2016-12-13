import hashlib

my = 'cxdnnyjw'
pw = ''
prev = 0

for i in range(8):
	cur = prev
	while True:
		cur += 1
		s = my + str(cur)
		m = hashlib.md5()
		m.update(s.encode('utf-8'))
		h = m.hexdigest()
		if h.startswith('00000'):
			pw += h[5]
			prev = cur
			print(pw)
			break
			
print(pw)