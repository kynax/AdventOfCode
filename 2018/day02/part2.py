import sys

def nb_diffs(s,p):
	total = 0
	for i in range(len(s)):
		if s[i] != p[i]:
			total += 1
		if total > 1:
			break
			
	return total
	
lines = []
for l in sys.stdin:
	lines.append(l.strip())
	
for i in range(len(lines)):
	for j in range(i + 1, len(lines)):
		if nb_diffs(lines[i], lines[j]) == 1:
			print(lines[i], lines[j])
			break