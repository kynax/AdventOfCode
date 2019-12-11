import sys

class Obj:
    def __init__(self, name):
        self.name = name
        self.down = []
        
    def add_child(self, obj):
        self.down.append(obj)
    
    def find(self, prev, target):
        if self.name == target:
            return prev + '-' + self.name
        else:
            for d in self.down:
                r = d.find(prev + '-' + self.name, target)
                if r is not None:
                    return r
        
    
    def distance(self, start):
        
        d = start
        
        if not self.down:
            print(self.name, start)
            
        for n in self.down:
            d += n.distance(start + 1)
            
        return d
        

COM = Obj('COM')
orbits = {}
orbits['COM'] = COM
effects = [x.strip().split(')') for x in list(sys.stdin)]

for c,o in effects:
    obj = None
    
    if o in orbits:
        obj = orbits[o]
    else:
        obj = Obj(o)
        orbits[o] = obj
        
    if c in orbits:
        orbits[c].add_child(obj)
    else:
        ctr = Obj(c)
        ctr.add_child(obj)
        orbits[c] = ctr
        
you = COM.find('', 'YOU')
san = COM.find('', 'SAN')

you = you[1:].split('-')
san = san[1:].split('-')

i = 0
while you[i] == san[i]:
    i += 1
    
print(len(you[i:]) + len(san[i:]) - 2)