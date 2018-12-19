import sys 

data = [int(c) for c in sys.stdin.readline().split(' ')]

total = 0

def process(d, t):
	nb_child = d.pop(0)
	nb_meta = d.pop(0)
	
	# if no child, score is total of metadata
	if nb_child == 0:
		for i in range(nb_meta):
			t += d.pop(0)
		return d,t
		
	# if child, sum child nodes
	child = []
	for i in range(nb_child):
		d,t = process(d,t)
		child.append(t)
	
	for i in range(nb_meta):
		idx = d.pop(0)
		if idx >= 0 and idx < len(child):
			t += child[idx]
	
	return d,t
	

total = process(data,0)
		
print(total)