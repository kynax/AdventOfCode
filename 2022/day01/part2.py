import sys

max = [0,0,0]
cur = 0
for l in sys.stdin:
    if l.strip() == '':
        if any( [cur > m for m in max] ):
            max.remove(min(max))
            max.append(cur)
        cur = 0
        continue

    cur += int(l.strip())

print(sum(max))