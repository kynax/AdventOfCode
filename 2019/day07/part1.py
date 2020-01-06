import sys
from intcode import *

m = [int(l) for l in sys.stdin.readline().split(',')]

aa = IntCode()
ab = IntCode()
ac = IntCode()
ad = IntCode()
ae = IntCode()
ra = 0
rb = 0
rc = 0
rd = 0
re = 0
best = 0
bestval = 0

for a in range(5):
    aa = IntCode()
    aa.mem_init(m)
    aa.add_input(a)
    aa.add_input(0)
    ra = aa.output()
    
    for b in range(5):
        if a == b:
            continue
            
        ab = IntCode()
        ab.mem_init(m)
        ab.add_input(b)
        ab.add_input(ra)
        rb = ab.output()
    
        for c in range(5):
            if c in [a,b]:
                continue
            
            ac = IntCode()
            ac.mem_init(m)
            ac.add_input(c)
            ac.add_input(rb)
            rc = ac.output()
    
            for d in range(5):
                if d in [a,b,c]:
                    continue
                
                ad = IntCode()
                ad.mem_init(m)
                ad.add_input(d)
                ad.add_input(rc)
                rd = ad.output()
                    
                for e in range(5):
                    if e in [a,b,c,d]:
                        continue
                
                    ae = IntCode()
                    ae.mem_init(m)
                    ae.add_input(e)
                    ae.add_input(rd)
                    re = ae.output()
                    
                    val = a * 10000 + b * 1000 + c * 100 + d * 10 + e
                    st = str(val)
                    if re > best:
                        best = re
                        bestval = val
                            
                            
print('Max thruster signal',best, 'from phase sequence', bestval)