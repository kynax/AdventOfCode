import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def rotate(name, n):
    ret = ''
    for c in name:
        if c == '-':
            ret += ' '
            continue
        ret += alphabet[(alphabet.index(c) + n) % 26]
    return ret


for l in sys.stdin:
    l = l.strip()
    lastdash = l.rindex('-')
    name = l[0:lastdash]
    #name = name.replace('-','')

    check = l[-6:-1]

    sector = int(l[lastdash+1:-7])

    decr = rotate(name,sector)
    if 'orth' in decr:
        print(decr, sector)