import sys 

def m_print(monkeys):
    for i in range(len(monkeys)):
        print('Monkey', i, ':', ', '.join([str(s) for s in monkeys[i]['items']]))

def test(l, val):
    t = int(l.split(' ')[3])
    return (val % t) == 0

def op(l,val):
    o,n = l.split(' ')[4:6]
    if 'old * old' in l:
        return val * val
    elif o == '*':
        return val * int(n)
    else:
        return val + int(n)

rounds = 10000
monkeys = []
monkey = {}
for l in sys.stdin:
    l = l.strip()

    if 'Starting' in l:
        monkey['items'] = [int(i) for i in l[15:].split(', ')]
        continue
    if 'Operation' in l:
        monkey['op'] = l
        continue
    if 'Test' in l:
        monkey['test'] = l
        continue
    if 'true' in l:
        monkey['true'] = int(l.split(' ')[5])
        continue
    if 'false' in l:
        monkey['false'] = int(l.split(' ')[5])
        monkey['count'] = 0
        monkeys.append(dict(monkey))
        continue

sm = 1
for m in monkeys:
    sm *= int(m['test'].split(' ')[3])

for r in range(rounds):
    for m in monkeys:
        for i in m['items']:
            t = op(m['op'], i)
            t = t % sm
            m['count'] += 1
            if test(m['test'], t):
                monkeys[m['true']]['items'].append(t)
            else:
                monkeys[m['false']]['items'].append(t)

        m['items'] = []

a,b = sorted([m['count'] for m in monkeys])[-2:]
print(a,b)
print(a*b)