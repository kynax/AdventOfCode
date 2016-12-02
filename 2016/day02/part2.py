import sys
cur = 11
forbidden = [1,2,4,5,6,10,16,20,21,22,24,25]
password = ''

pos = {3 : '1', 7:'2',8:'3',9:'4',11:'5',12:'6',13:'7',14:'8',15:'9',17:'A',18:'B',19:'C',23:'D'}


for line in sys.stdin:	
	for d in line:
		if d == 'D' and cur < 21 and cur + 5 not in forbidden:
			cur += 5
		if d == 'U' and cur > 5 and cur - 5 not in forbidden:
			cur -= 5
		if d == 'L' and cur % 5 != 1 and cur - 1 not in forbidden:
			cur -= 1
		if d == 'R' and cur % 5 != 0 and cur + 1 not in forbidden:
			cur += 1
	password += pos[cur]

print(password)