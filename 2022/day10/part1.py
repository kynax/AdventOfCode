import sys

cycle = 0
acc = 1
signal = 0
for l in sys.stdin:
    l = l.strip()

    wait = 1
    if l == 'noop':
        new_val = acc
    else:
        wait = 2
        new_val = int(l.split(' ')[1]) + acc

    for w in range(wait):
        cycle += 1
        if cycle % 40 - 20 == 0:
            signal += acc*cycle

    acc = new_val

print(signal)

