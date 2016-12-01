alpha = list('abcdefghijklmnopqrstuvwxyz')
input = list("vzbxkghb")
again = list("vzbxxyzz")

def next(s):
	n = s
	last = len(input)-1
	done = False
	while not done:
		if n[last] == 'z':
			n[last] = 'a'
			last -= 1
		else:
			n[last] = alpha[alpha.index(n[last])+1]
			done = True
	return n

def isValid(s):
	increasing = False
	for i in range(len(s)-2):
		if alpha.index(s[i]) + 1 == alpha.index(s[i+1]) and alpha.index(s[i]) + 2 == alpha.index(s[i+2]):
			increasing = True
			break
	if not increasing:
		return False
	
	if 'i' in s or 'o' in s or 'l' in s:
		return False
		
	pairs = 0
	i = 0
	while i < len(s) - 1:
		if s[i] == s[i+1]:
			pairs += 1
			i += 1
		i += 1
	if pairs < 2:
		return False
		
	return True

n = next(again)
while not isValid(n):
	n = next(n)
print(n)