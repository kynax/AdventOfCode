import sys
from collections import Counter

lines = []

for l in sys.stdin:
	lines.append(l.strip())
	
lines.sort()

schedule = {}
guard = -1
asleep = -1

for l in lines:
	if 'begins shift' in l:
		guard = l[l.index('#')+1:]
		guard = int(guard[:guard.index(' ')])
		#print("guard", guard, "takes over")
		
	if 'falls asleep' in l:
		#print('asleep at', l[15:17])
		asleep = int(l[15:17])
		
	if 'wakes up' in l:
		#print('wakes up at', l[15:17])
		if guard not in schedule:
			schedule[guard] = []
		for i in range(asleep, int(l[15:17])):
			schedule[guard].append(i)

sleepiest = 0
frequent = 	0	
id_freq = 0
min_freq = 0

for (k,v) in schedule.items():
	if sleepiest == 0:
		sleepiest = k
		continue
		
	if id_freq == 0:
		id_freq = k
	
	if len(v) > len(schedule[sleepiest]):
		sleepiest = k
		
	c = Counter(schedule[k]).most_common(1)[0]
	if c[1] > frequent:
		frequent = c[1]
		min_freq = c[0]
		id_freq = k

# part 1
print('part 1')
print('guard', sleepiest)
print('minute', Counter(schedule[sleepiest]).most_common(1)[0][0])
print('answer', sleepiest * Counter(schedule[sleepiest]).most_common(1)[0][0])
print()

# part 2
print('part 2')
print('guard', id_freq)
print('most freq', min_freq)
print('answer', min_freq * id_freq)
