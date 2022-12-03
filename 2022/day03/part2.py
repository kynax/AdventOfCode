import sys

value = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = 0
l = [l.strip() for l in sys.stdin]

for i in range(0, len(l), 3):

    for v in value:
        if v in l[i] and v in l[i+1] and v in l[i+2]:
            total += value.index(v)

print(total)