import sys 

data = [int(c) for c in sys.stdin.readline().split(' ')]

total = 0

def process(d, t):
	nb_child = d.pop(0)
	nb_meta = d.pop(0)
	for i in range(nb_child):
		d,t = process(d,t)
	for i in range(nb_meta):
		t += d.pop(0)
	return d,t
	

total = process(data,0)
		
print(total)