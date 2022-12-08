import sys

grid = [ [int(c) for c in l.strip()] for l in sys.stdin]
sx = len(grid[0])
sy = len(grid)

visibles = []
for row in range(sy):
    # left to right
    high = -1
    for i in range(sx):
        if grid[row][i] > high:
            if (i,row) not in visibles:
                visibles.append( (i, row) )
            high = grid[row][i]
    
    # right to left
    high = -1
    for i in range(sx-1, -1, -1):
        if grid[row][i] > high:
            if (i,row) not in visibles:
                visibles.append( (i, row) )
            high = grid[row][i]

for col in range(sx):
    # left to right
    high = -1
    for i in range(sy):
        if grid[i][col] > high:
            if (col,i) not in visibles:
                visibles.append( (col,i) )
            high = grid[i][col]
    
    # right to left
    high = -1
    for i in range(sy-1, -1, -1):
        if grid[i][col] > high:
            if(col,i) not in visibles:
                visibles.append( (col,i) )
            high = grid[i][col]

#print(visibles)
print(len(visibles))