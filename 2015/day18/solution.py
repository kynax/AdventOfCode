def solve(part):
    a = []

    for l in open('input.txt'):
        a.append([1 if c == '#' else 0 for c in l.strip()])

    maxlen = len(l.strip())

    if part == 2:
        a[0][0] = 1
        a[maxlen-1][0] = 1
        a[0][maxlen-1] = 1
        a[maxlen-1][maxlen-1] = 1
    for b in range(100):
        change = []
        for d in range(maxlen):
            for c in range(maxlen):
                s = 0
                for n in [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]:
                    if c+n[0] >= 0 and c+n[0] < maxlen and d+n[1] >= 0 and d+n[1] < maxlen:
                        if a[c+n[0]][d+n[1]] == 1:
                            s += 1
                if a[c][d] == 1 and s < 2 or s > 3:
                    if part == 1 or [c,d] not in [[0,0], [maxlen-1,0], [0,maxlen-1], [maxlen-1,maxlen-1]]:
                        change.append([c,d,0])
                if a[c][d] == 0 and s == 3:
                    change.append([c,d,1])
        for i in change:
            a[i[0]][i[1]] = i[2]
    return sum(sum(a, []))

print (solve(1))
print (solve(2))