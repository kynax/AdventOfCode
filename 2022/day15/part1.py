import sys

grid = {}
sensitivity = []
sensors = []
beacons = []

for l in sys.stdin:
    l = l.strip().split(' ')
    sx, sy, bx, by = int(l[2][2:-1]), int(l[3][2:-1]), int(l[8][2:-1]), int(l[9][2:])
    
    grid[(sx,sy)] = 'S'
    grid[(bx,by)] = 'B'
    dx,dy = abs(sx-bx), abs(sy-by)
    md = dx+dy

    sensitivity.append((sx,sy,md))
    sensors.append((sx,sy))
    if (bx,by) not in beacons: beacons.append((bx,by))

minx = min([i[0]-i[2] for i in sensitivity])-1
maxx = max([i[0]+i[2] for i in sensitivity])+1
row = 2000000
#row = 10 # example

intervals = []
for s in sensitivity:
    d = abs(s[1] - row)
    w = s[2] - d
    b,e = s[0] - w, s[0] + w
    if e < b: b,e = e,b
    intervals.append((b,e))
ints = sorted(intervals)

nints = [ints[0]]
for i in range(1, len(ints)):
    if ints[i][0] <= nints[-1][1]:
        if ints[i][1] <= nints[-1][1]:
            pass # fully included
        else:
            nints[-1] = (nints[-1][0], ints[i][1])
    else:
        nints.append(ints[i])

score = sum([i[1]-i[0]+1 
        - sum([1 for b in beacons if b[1] == row and b[0] >= i[0] and b[0] <= i[1]]) 
        - sum([1 for s in sensors if s[1] == row and s[0] >= i[0] and s[0] <= i[1]]) 
        for i in nints])
print(score)