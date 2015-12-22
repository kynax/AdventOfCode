import sys
import itertools

containers = []
total = 150
cur = 0
success = 0

### part 2 ###
count = 99999
### 

for line in sys.stdin:
	containers.append(int(line))
	
containers.sort()

for c in itertools.chain.from_iterable(itertools.combinations(containers, r) for r in range(len(containers)+1)):
	if sum(c) == 150 and len(c) <= count:
		success += 1
	### part 2
		count = len(c)
	if len(c) > count:
		break
	###
		
print(success)