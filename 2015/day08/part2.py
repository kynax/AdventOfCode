import sys

raw = 0
total = 0

for line in sys.stdin:
	word = line.strip()
	raw += len(word)
	total += 2 + word.count('"') + word.count('\\') + len(word)
	print(len(word), 2 + word.count('"') + word.count('\\') + len(word))

print(total - raw)