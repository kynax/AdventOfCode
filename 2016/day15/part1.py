import sys

discs = []

for l in sys.stdin:
    s = l.split()
    discs.append((int(s[3]),int(s[11][:-1])))

for i in range(100000000):
    found = True
    for d in range(len(discs)):
        if (discs[d][1] + i + d + 1) % discs[d][0] != 0:
            found = False
            break
    if found:
        print(i)
        break