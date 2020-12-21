import sys

# key = bags, values = valid containers
bags = {}
for l in sys.stdin:
	s = l.strip().split(' bags contain ')
	container = s[0]
	bgs = s[1][:-1].split(', ')
	
	if bgs[0] == 'no other bags':
		continue
		
	for b in bgs:
		b = b[2:].replace('bags','').replace('bag','').strip()
		if b not in bags:
			bags[b] = set()
		bags[b].add(container)
print(bags)
outer = []
outer.append('shiny gold')
added = True
while added:
	added = False
	for b in outer:
		if b in bags:
			for i in bags[b]:
				if i not in outer:
					outer.append(i)
					added = True
				
print(len(outer)-1)
	