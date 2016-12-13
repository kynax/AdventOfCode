import hashlib

my = 'cxdnnyjw'
pw = ['_','_','_','_','_','_','_','_']
idx = [0,1,2,3,4,5,6,7]
cur = 0

while True:

	while True:
		cur += 1
		s = my + str(cur)
		m = hashlib.md5()
		m.update(s.encode('utf-8'))
		h = m.hexdigest()
		if h.startswith('00000') and h[5] in '0123456789' and int(h[5]) >= 0 and int(h[5]) < 9:
			
			if int(h[5]) in idx:
				pw[int(h[5])] = h[6]
				idx.remove(int(h[5]))
				print(''.join(pw), "at", cur)
			
			break
			
	if len(idx) == 0:
		break
			
print(pw)