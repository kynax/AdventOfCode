import sys
from collections import Counter

total = 0

def compare(x,y):
    if x[1] > y[1]:
        return -1
    if y[1] > x[1]:
        return 1
    if x[0] < y[0]:
        return -1
    if x[0] > y[0]:
        return 1
    return 0

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def isReal(name, check):
    most = list(x[0] for x in sorted(Counter(name).most_common(), key=cmp_to_key(compare))[:5])
    
    for c in most:
        if c not in check:
            return False
    return True


for l in sys.stdin:
    l = l.strip()
    lastdash = l.rindex('-')
    name = l[0:lastdash]
    name = name.replace('-','')

    check = l[-6:-1]

    sector = int(l[lastdash+1:-7])

    if isReal(name, check):
        total += sector
print(total)