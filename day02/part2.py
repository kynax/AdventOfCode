import sys
total = 0
for line in sys.stdin:
	dims = line.split('x')
	w = int(dims[0])
	l = int(dims[1])
	h = int(dims[2])
	bow = w * l * h
	rib = (w + l + h - max(w,l,h)) * 2
	total = total + rib + bow
print(total)