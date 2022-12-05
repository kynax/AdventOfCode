import sys

lines = [l.rstrip() for l in sys.stdin]

grid = lines[:lines.index('')]

stacks = [ [] for i in range(10) ]
for g in range(len(grid)-2, -1, -1) :
    for i in range(1, 34, 4):
        l = grid[g].ljust(34, ' ')
        if l[i] == ' ':
            continue
        stacks[i//4 +1].append(l[i])

steps = lines[lines.index('')+1:]
for s in steps:
    _, nb, _, src, _, dst = s.split(' ')
    nb, src, dst = int(nb), int(src), int(dst)
    for n in range(nb):
        stacks[dst].append(stacks[src].pop())

print(''.join([s[-1] if len(s)>0 else '' for s in stacks]))