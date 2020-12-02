import sys

total = 0
for l in sys.stdin:
	(count, letter, pwd) = l.strip().split(' ')
	(min, max) = count.split('-')
	(min, max) = (int(min), int(max))
	letter = letter[:-1]
	
	if (pwd[min - 1] == letter and pwd[max - 1] != letter) or (pwd[min - 1] != letter and pwd[max - 1] == letter):
		total += 1
		
print(total)