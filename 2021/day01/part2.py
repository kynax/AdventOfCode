import sys

prev = 999999
total = 0
nums = [int(l.strip()) for l in sys.stdin]

for i in range(1, len(nums)-1):
	cur = nums[i-1] + nums[i] + nums[i+1]
	if cur > prev:
		total += 1
	prev = cur
	
print(total)