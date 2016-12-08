import sys

t = 0
l = []
m = []
r = []


for line in sys.stdin:
	i = [int(s) for s in line.split()]
	l.append(i[0])
	m.append(i[1])
	r.append(i[2])
	if len(l) == 3:
		if sum(l) - max(l) > max(l):
			t += 1
		if sum(m) - max(m) > max(m):
			t += 1
		if sum(r) - max(r) > max(r):
			t += 1
		l = []
		m = []
		r = []
print(t)