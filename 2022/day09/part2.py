import sys

visited = [(0,0)]
parts = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
for l in sys.stdin:
    dir, nb = l.strip().split(' ')
    
    for i in range(int(nb)):
        head = parts[0]
        if dir == 'U':
            head = (head[0], head[1]+1)
        elif dir == 'D':
            head = (head[0], head[1]-1)
        elif dir == 'L':
            head = (head[0]-1, head[1])
        elif dir == 'R':
            head = (head[0]+1, head[1])

        parts[0] = head
        for i in range(0,9):
            head = parts[i]
            tail = parts[i+1]
            dx,dy = head[0] - tail[0], head[1] - tail[1]
            adx, ady = abs(dx), abs(dy)
            
            if adx < 2 and ady < 2:
                pass
            elif adx != 0 and ady == 0:
                tail = (tail[0] + dx//adx, tail[1])
            elif adx == 0 and ady != 0:
                tail = (tail[0], tail[1] + dy//ady)
            else:
                tail = (tail[0] + dx//adx, tail[1] + dy//ady)
            parts[i+1] = tail
        

        if tail not in visited:
            visited.append(tail)

print(len(visited))