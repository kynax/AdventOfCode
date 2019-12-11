import sys

class Obj:
    def __init__(self, name):
        self.name = name
        self.down = []
        
    def add_child(self, obj):
        self.down.append(obj)
    
    def prnt(self, prev):
        if not self.down:
            print(prev + '=' + self.name)
        else:
            for d in self.down:
                d.prnt(prev + '-' + self.name)
        
    
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
        
print(COM.distance(0))
