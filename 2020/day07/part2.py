import sys

# key = container, values = contents
bags = {}
for l in sys.stdin:
	s = l.strip().split(' bags contain ')
	container = s[0]
	bgs = s[1].replace(' bags','').replace(' bag','').strip()[:-1].split(', ')
	
	if bgs[0] == 'no other':
		continue
	
	bags[container] = bgs
	
def count(bag, bags):
	if bag not in bags:
		return 1
	
	ret = 1 # itself
	# plus all inside
	for b in bags[bag]:
		ret += int(b[0]) * count(b[2:], bags)
	return ret
		
print(count('shiny gold', bags) - 1) # minus initial bag