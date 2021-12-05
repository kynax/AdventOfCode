import sys

c = [0 for x in range(13)]

def filter(nums, target, up):
	
	t = sum([x[target] for x in nums])
	
	invert = 1
	if not up:
		invert = -1
		
	if t >= 0: # on cherche ceux qui ont le 1
		n = [x for x in nums if x[target] == 1*invert]
	else:
		# sinon c'est les zéros qui ont gagné
		n = [x for x in nums if x[target] == -1*invert]
	
	if len(n) == 1:
		return int(''.join(['1' if x == 1 else '0' for x in n[0]]),2)
	
	return filter(n, target+1, up)
	
	
	
nums = []
for l in sys.stdin:
	n = l.strip()
	
	nums.append([1 if x == '1' else -1 for x in n])

print(filter(nums, 0, True) * filter(nums, 0, False))
