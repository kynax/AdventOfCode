def issymbol(s, x, y):
    try:
        if s[x][y] == '*':
            return (x,y)
    except:
        return None

with open('input.txt') as f:
    lines = [l.strip() for l in f]

cur = 0
total = 0
gear = None
adj = [(0,1), (0,-1), (1,0), (-1,0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
gears = {}
for lnum in range(len(lines)):
    l = lines[lnum]
    for i in range(len(l)):

        if l[i].isdigit():
            cur = cur * 10 + int(l[i])
            try:
                gear = [g for g in [issymbol(lines, lnum+x, i+y) for x,y in adj] if g is not None][0]
            except:
                pass
        else:
            if cur > 0 and gear:
                if gear not in gears.keys():
                    gears[gear] = [cur]
                else:
                    gears[gear].append(cur)

            cur = 0
            gear = False

print(sum(x*y for x,y in [x for x in gears.values() if x is not None and len(x) == 2]))