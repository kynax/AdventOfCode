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

for row in range(4000000):
    intervals = []
    for s in sensitivity:
        d = abs(s[1] - row)
        if d > s[2]:
            continue
        w = s[2] - d
        b,e = s[0] - abs(w), s[0] + abs(w)
        if e < b: b,e = e,b
        intervals.append((b,e))
    ints = sorted(intervals)

    nints = [ints[0]]
    for i in range(1, len(ints)):
        if ints[i][0] <= nints[-1][1]+1:
            if ints[i][1] <= nints[-1][1]:
                pass # fully included
            else:
                nints[-1] = (nints[-1][0], ints[i][1])
        else:
            nints.append(ints[i])

    if len(nints) > 1:
        print(nints, nints[0][1] + 1, row)
        print(4000000 * (nints[0][1]+1) + row)
        break