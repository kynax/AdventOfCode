

def calc(n, max):
	nums = n
	for turn in range(len(nums)+1, max+1):
		prev = nums[turn-2]
		#print('cherche', prev)

		if not prev in nums[:-1]:
			nums.append(0)
			continue

		for i in range(len(nums)-2, -1, -1):
			if nums[i] == prev:
				nums.append(turn-i-2)
				break
	return nums[-1]

# tests - examples
print(calc([1,3,2], 2020))
print(calc([2,1,3], 2020))
print(calc([1,2,3], 2020))

print(calc([2,15,0,9,1,20], 2020))

print(calc([2,15,0,9,1,20], 30000000))