import sys

vowels = "aeiou"
no = ["ab", "cd", "pq", "xy"]
total = 0
for s in sys.stdin:
	nice = True
	for n in no:
		if n in s:
			nice = False
			break;
	if not nice:
		continue
	
	if sum(map(s.count, "aeiou")) < 3:
		continue
	
	nice = False
	for i in range(len(s) - 1):
		if s[i] == s[i+1]:
			nice = True
			
	if not nice:
		continue
	
	total += 1

print(total)