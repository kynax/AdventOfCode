import sys

def fold_y(pts, n):
	npts = {}
	for k,v in pts.items():
		if k[1] < n:
			npts[tuple([k[0], k[1]])] = '#'
		else:
			npts[tuple([k[0], n-(k[1] - n)])] = '#'
	return npts

def fold_x(pts, n):
	npts = {}
	for k,v in pts.items():
		if k[0] < n:
			npts[ tuple([k[0],k[1]]) ] = '#'
		else:
			npts[ tuple([n-(k[0]-n),k[1]]) ] = '#'
	return npts

def display(pts):
	mx = max(k[0] for k in pts.keys())+1
	my = max(k[1] for k in pts.keys())+1

	for y in range(my):
		s = ''
		for x in range(mx):
			if tuple([x,y]) in pts:
				s += '#'
			else:
				s += ' '
		print(s)
	
	

pts = {}
folds = None
for l in sys.stdin:
	if l.strip() == '':
		folds = []
		continue
		
	if folds is None:
		pts[ tuple(int(x) for x in l.strip().split(','))] = '#'
		continue
		
	if folds is not None:
		folds.append( l.strip().split(' ')[2].split('=') )
		folds[-1][1] = int(folds[-1][1])
		continue
				  

# part 2 : all folds
for f in folds:
	if f[0] == 'x':
		pts = fold_x(pts, f[1])
	else:
		pts = fold_y(pts, f[1])
		
display(pts)
		
# and print

		