import sys
time = 2503
deers = []
dists = {}
for line in sys.stdin:
	dist = 0 
	
	words = line.split()
	name = words[0]
	speed = int(words[3])
	duration = int(words[6])
	rest = int(words[13])
	deers.append((name,speed, duration, rest))
	dists[name] = 0

for i in range(1, time+1):
	leader = []
	best = 0
	cur = []
	for d in deers:
		rep_time = d[2] + d[3]
		rep_dist = d[1] * d[2]
		full_reps = int(i / rep_time)
		dist = full_reps * rep_dist
		
		remain = i % rep_time
		if remain > d[2]:
			dist += rep_dist
		else:
			dist += remain * d[1]
		
		print(d[0], "at", dist)
		cur.append((dist,d[0]))
		if dist > best:
			best = dist
	
	for val in cur:
		if val[0] == best:
			print("best", val[1])
			dists[val[1]] += 1
	print(dists)
	print()

best = 0	
for d in dists.keys():
	if dists[d] > best:
		 best = dists[d]

print(best)
