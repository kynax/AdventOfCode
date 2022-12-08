import sys

grid = [ [int(c) for c in l.strip()] for l in sys.stdin]
sx = len(grid[0])
sy = len(grid)

best = 0
for row in range(1, sy-1):
    for col in range(1, sx-1):
        score = 1
        me = grid[row][col]

        for x in range(col+1, sx, 1):
            if grid[row][x] >= me:
                break
        score *= x-col

        for x in range(col-1, -1, -1):
            if grid[row][x] >= me:
                break
        score *= col-x

        for y in range(row+1, sy, 1):
            if grid[y][col] >= me:
                break
        score *= y-row

        for y in range(row-1, -1, -1):
            if grid[y][col] >= me:
                break
        score *= row-y

        if score > best:
            best = score

print(best)