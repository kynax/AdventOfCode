import sys

value = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = 0


for l in sys.stdin:
    l = l.strip()
    a,b = l[:len(l)//2], l[len(l)//2:]

    for i in a:
        if i in b:
            total += value.index(i)
            break

    
print(total)