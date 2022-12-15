import sys

def my_print(grid):
    k = grid.keys()
    xs,ys = [i[0] for i in k], [i[1] for i in k]
    minx, maxx = min(xs)-1, max(xs)+1
    miny, maxy = min(ys)-1, max(ys)+1

    for y in range(0, maxy):
        s = ''
        for x in range(minx, maxx):
            if (x,y) in grid:
                s += grid[(x,y)]
            else:
                s += '.'
        print(s)

grid = {}
lines = [l.strip() for l in sys.stdin]
for l in lines:
    pts = l.split(' -> ')
    for i in range(len(pts)-1):
        startx, starty = pts[i].split(',')
        stopx, stopy = pts[i+1].split(',')
        startx, starty, stopx, stopy = int(startx), int(starty), int(stopx), int(stopy)
        dx,dy = stopx - startx, stopy - starty
        adx, ady = abs(dx), abs(dy)

        for i in range(max(adx, ady)+1):
            grid[(startx+(i*(dx//(adx+ady))), starty+(i*(dy//(adx+ady))))] = '#'

maxy = max([i[1] for i in grid.keys()])
one_more = True
#my_print(grid)
while one_more:
    if (500,0) in grid:
        break
    posx, posy = 500, 0
    while True:
        if (posx, posy+1) not in grid or grid[(posx, posy+1)] == '.':
            posy += 1
        elif (posx-1,posy+1) not in grid or grid[(posx-1,posy+1)] == '.':
            posx -= 1
            posy += 1
        elif (posx+1, posy+1) not in grid or grid[(posx+1, posy+1)] == '.':
            posx += 1
            posy += 1
        else:
            grid[(posx,posy)] = 'o'
            break
        if posy > maxy:
            grid[(posx,posy)] = 'o'
            break

#my_print(grid)
print(sum([1 for x in grid.values() if x == 'o']))
