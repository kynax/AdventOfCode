import sys

total = 0
for l in sys.stdin:
	(count, letter, pwd) = l.strip().split(' ')
	(min, max) = count.split('-')
	(min, max) = (int(min), int(max))
	letter = letter[:-1]
	
	test = pwd.count(letter)
	
	#print(pwd, letter, min, max, test)
	
	if test >= min and test <= max:
		total += 1
		
print(total)