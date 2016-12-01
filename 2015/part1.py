import hashlib
key = "ckczppom"

for i in range(10000000):
	m = hashlib.md5()
	m.update((key + str(i)).encode('utf-8'))
	digest = m.hexdigest()
	if digest.startswith("000000"):
		print(digest)
		print(i)
		break