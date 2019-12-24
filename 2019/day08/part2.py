import sys

l = sys.stdin.readline()

size = 25 * 6

layers = []

for layer in range(len(l) // size):
    values = [int(x) for x in l[layer * size : layer * size + size ]]
    layers.append(values)
    
color = ' '
line = ""
for y in range(6):
    for x in range(25):
        color = ' '
        for l in layers:
            if l[x + y * 25] == 2:
                continue
            else:
                color = ' ' if l[x + y * 25] == 0 else 'X'
                break
        line += color
    print(line)
    line = ""
    