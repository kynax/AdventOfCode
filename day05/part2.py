import sys
total = 0
for s in sys.stdin:
	repeat = False
	for i in range(len(s) - 2):
		if s[i] == s[i+2]:
			repeat = True
			break
			
	if not repeat:
		continue
	
	pair = False
	for i in range(len(s) - 2):
		if s[i:i+2] in s[i+2:]:
			pair = True
			break
	
	if not pair:
		continue
	
	total += 1
print(total)