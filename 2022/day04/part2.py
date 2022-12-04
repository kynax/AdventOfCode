import sys

tot = 0
for l in sys.stdin:
    a,b = l.strip().split(',')
    a1,a2 = [int(x) for x in a.split('-')]
    b1,b2 = [int(x) for x in b.split('-')]

    if (a1 >= b1 and a1 <= b2) or (b1 >= a1 and b1 <= a2):
        tot += 1

print(tot)