import sys

mins = []
maxs = []

# load start/end of intervals
for l in sys.stdin:
	s = l.split('-')
	mins.append(int(s[0]))
	maxs.append(int(s[1]))
	
# find first max
max = 0
for i in range(len(mins)):
	if mins[i] == 0:
		max = maxs[i]

# keep expanding
go = True
while go:
	go = False
	for i in range(len(mins)):
		if mins[i] <= max+1:
			if maxs[i] > max:
				max = maxs[i]
				print("Expanding to", max)
				go = True
print(max+1)
