import sys
cur = 5
password = ''

for line in sys.stdin:	
	for d in line:
		if d == 'D' and cur < 7:
			cur += 3
		if d == 'U' and cur > 3:
			cur -= 3
		if d == 'L' and cur % 3 != 1:
			cur -= 1
		if d == 'R' and cur % 3 != 0:
			cur += 1
	password += str(cur)

print(password)