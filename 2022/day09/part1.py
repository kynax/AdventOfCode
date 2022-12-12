import sys

visited = [(0,0)]
head = (0,0)
tail = (0,0)
for l in sys.stdin:
    dir, nb = l.strip().split(' ')
    
    for i in range(int(nb)):
        if dir == 'U':
            head = (head[0], head[1]+1)
        elif dir == 'D':
            head = (head[0], head[1]-1)
        elif dir == 'L':
            head = (head[0]-1, head[1])
        elif dir == 'R':
            head = (head[0]+1, head[1])

        dx,dy = head[0] - tail[0], head[1] - tail[1]
        adx, ady = abs(dx), abs(dy)
        
        if adx < 2 and ady < 2:
            pass
        elif adx == 2 and ady == 0:
            tail = (tail[0] + dx//adx, tail[1])
        elif adx == 0 and ady == 2:
            tail = (tail[0], tail[1] + dy//ady)
        else:
            tail = (tail[0] + dx//adx, tail[1] + dy//ady)
        
        if tail not in visited:
            visited.append(tail)

print(len(visited))