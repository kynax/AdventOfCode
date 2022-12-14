import sys

def my_print(grid):
    for l in grid:
        print(' '.join([str(i[1]).ljust(2) if i[1] is not None else '  ' for i in l]))

end = ord('E')
sta = ord('S')
pos_end = None
pos_sta = None

grid = [[[ord(c), None] for c in l.strip()] for l in sys.stdin]
sx, sy = len(grid[0]), len(grid)

for y in range(sy):
    for x in range(sx):
        if grid[y][x][0] == end:
            pos_end = (x,y)
            grid[y][x][1] = 0
        if grid[y][x][0] == sta:
            pos_sta = (x,y)

grid[pos_sta[1]][pos_sta[0]][0] = ord('a')
grid[pos_end[1]][pos_end[0]][0] = ord('z')

done = False
while not done:
    done = True
    for y in range(sy):
        for x in range(sx):
            best = 999999999
            here, path = grid[y][x]
            # check all neighbors
            # for better path
            if x+1 < sx and grid[y][x+1][0] -1 <= here and grid[y][x+1][1] is not None: best = min(best, grid[y][x+1][1])
            if x-1 >= 0 and grid[y][x-1][0] -1 <= here and grid[y][x-1][1] is not None: best = min(best, grid[y][x-1][1])
            if y+1 < sy and grid[y+1][x][0] -1 <= here and grid[y+1][x][1] is not None: best = min(best, grid[y+1][x][1])
            if y-1 >= 0 and grid[y-1][x][0] -1 <= here and grid[y-1][x][1] is not None: best = min(best, grid[y-1][x][1])
            if best != 999999999 and (path is None or best+1 < path):
                grid[y][x][1] = best+1
                done = False

best_a = (0, 999999999)
for l in grid:
    for g in l:
        if g[0] == ord('a') and g[1] is not None and g[1] < best_a[1]:
            best_a = g

print(best_a[1])