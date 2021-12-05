import sys

l = sys.stdin.readlines()

nums = [int(x) for x in l[0].strip().split(',')]

l = l[2:]

lines = []

for g in range(0,len(l),6):
	gridlines = [[int(x) for x in s.strip().replace('  ',' ').split()] for s in l[g:g+5]]

	for r in gridlines:
		lines.append( (g // 6, r) )
		
	for c in [[gridlines[i][x] for i in range(5)] for x in range(5)]:
		lines.append( (g // 6, c) )
		
for n in range(4, len(nums)):
	
	for gridno, line in lines:
		if all(x in nums[:n] for x in line):
			print('grid', gridno, 'nums', nums[:n])
			
			total = 0
			for winningline in [x for (no,x) in lines if no == gridno]:
				for no in winningline:
					if no not in nums[:n]:
						total += no
			print(total // 2 * nums[n-1])
			exit()

print('failed')