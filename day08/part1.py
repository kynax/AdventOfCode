import sys

raw = 0
total = 0

for line in sys.stdin:
	word = line.strip()
	raw += len(word)
	
	word = word[1:-1].replace("\\\\", "!")
	word = word.replace('\\"', '*')
	l = len(word)
	escapes = word.count('\\x') * 3
	l -= escapes
	total += l 
	
	print(raw, l)
	
		
print(raw - total)