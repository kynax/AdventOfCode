import sys

def draw(grid, l, wire):
    
    x = 0
    y = 0
    dx = 0
    dy = 0
    length = 0
    for i in l.split(','):
        d = i[0:1]
        c = int(i[1:])
        if d == 'U':
            dy = 1
            dx = 0
        elif d == 'D':
            dy = -1
            dx = 0
        elif d == 'L':
            dy = 0
            dx = -1
        elif d == 'R':
            dy = 0
            dx = 1
        
        for z in range(c):
            x = x + dx
            y = y + dy
            length = length + 1
            if (x,y) in grid.keys() and wire not in grid[(x,y)]:
                grid[(x,y)][wire] = length
            else:
                grid[(x,y)] = {wire: length}

grid = {(0,0): 'o'}
l = sys.stdin.readline()
#l = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
#l = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
#l = 'R8,U5,L5,D3'
draw(grid, l, 1)
l = sys.stdin.readline()
#l = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
#l = 'U62,R66,U55,R34,D71,R55,D58,R83'
#l = 'U7,R6,D4,L4'
draw(grid, l, 2)

d = []
for k,v in grid.items():
    if len(v) == 2:
        print(v)
        d.append(v[1] + v[2])
        
print(min(d))