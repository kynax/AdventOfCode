start = str(input())

def Step(s):
	cur = s[0]
	count = 0
	ret = ""
	for c in s:
		if c != cur and cur != '':
			ret += str(count) + cur
			count = 0
			cur = c
		count += 1
	ret += str(count) + cur
	return ret

for i in range(50):
	start = Step(start)
print(len(start))