def issymbol(s, x, y):
    try:
        return s[x][y] != '.' and not s[x][y].isdigit()
    except:
        return False

with open('input.txt') as f:
    lines = [l.strip() for l in f]

cur = 0
valid = False
total = 0
adj = [(0,1), (0,-1), (1,0), (-1,0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
for lnum in range(len(lines)):
    l = lines[lnum]
    for i in range(len(l)):

        if l[i].isdigit():
            cur = cur * 10 + int(l[i])
            if not valid:
                valid = any(issymbol(lines, lnum+x, i+y) for x,y in adj)
        else:
            if cur > 0 and valid:
                total = total + cur
            cur = 0
            valid = False

print(total)