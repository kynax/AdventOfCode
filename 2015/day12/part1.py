import sys
valid = '1234567890-'
total = 0
cur = ''
for line in sys.stdin:
	for c in line:
		if c in valid:
			cur += c
		else:
			if cur != '':
				print(cur)
				total += int(cur)
				cur = ''
			
print(total)