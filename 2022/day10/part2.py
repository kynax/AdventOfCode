import sys

cycle = 0
acc = 1
signal = 0
crt = ''
for l in sys.stdin:
    l = l.strip()

    wait = 1
    if l == 'noop':
        new_val = acc
    else:
        wait = 2
        new_val = int(l.split(' ')[1]) + acc

    for w in range(wait):  

        if cycle % 40 in (acc-1, acc, acc+1):
            crt += '#'
        else:
            crt += ' ' 

        if len(crt) == 40:
            print(crt)
            crt = ''

        cycle += 1

    acc = new_val


print()

