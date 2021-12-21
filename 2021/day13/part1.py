import sys

def fold_y(pts, n):
	npts = {}
	for k,v in pts.items():
		npts[ tuple([k[0], abs(k[1] - n)]) ] = '#'
	return npts

def fold_x(pts, n):
	npts = {}
	for k,v in pts.items():
		npts[ tuple([abs(k[0]-n), k[1]]) ] = '#'
	return npts
	

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
				  

# part 1 : just the first fold
if folds[0][0] == 'x':
	print(len(fold_x(pts, folds[0][1])))
else:
	print(len(fold_y(pts, folds[0][1])))
				   
		