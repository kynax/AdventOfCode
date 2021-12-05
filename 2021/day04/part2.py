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
		
for n in range(4, len(nums)+1):
	
	for gridno, line in lines:
		if all(x in nums[:n] for x in line):
			if len(lines) > 10: # s'il reste plusieurs boards, on retire celle qui vient de gagner
				lines = [l for l in lines if l[0] != gridno]
			else:
				# la dernière board vient de gagner, on compte son score
				total = 0
				for winningline in [x for (no,x) in lines]:
					for no in winningline:
						if no not in nums[:n]:
							total += no
				print(total // 2 * nums[n-1])
				exit()

print('failed')