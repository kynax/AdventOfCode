import sys
total = 0
for line in sys.stdin:
	dims = line.split('x')
	w = int(dims[0])
	l = int(dims[1])
	h = int(dims[2])
	a1 = l * w
	a2 = w * h
	a3 = h * l
	sl = min(a1,a2,a3)
	rq = 2 * a1 + 2 * a2 + 2 * a3 + sl
	total = total + rq
print(total)