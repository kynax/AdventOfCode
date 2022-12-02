import sys

max = 0
cur = 0
for l in sys.stdin:
    if l.strip() == '':
        if cur > max:
            max = cur
        cur = 0
        continue

    cur += int(l.strip())

print(max)