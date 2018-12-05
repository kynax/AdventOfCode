import sys

i = 0
s = sys.stdin.read().strip()

def process(s):
	again = True
	while again:
		again = False
		for i in range(len(s)-1):
			if abs(ord(s[i]) - ord(s[i+1])) == 32:
				again = True
				s = s[:i] + s[i+2:]
				break
	return s

# part 1
print('-', len(process(s)))

# part 2
for i in range(ord('A'), ord('Z') + 1):
	print(chr(i), len(process(s.replace(chr(i), '').replace(chr(i+32),''))))