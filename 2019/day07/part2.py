import sys
from intcode import *
import itertools

m = [int(l) for l in sys.stdin.readline().split(',')]

settings = [5,6,7,8,9]

bestseq = 0
bestval = 0

for p in itertools.permutations(settings):
    amps = []
    for i in p:
        amp = IntCode()
        amp.mem_init(m)
        amp.add_input(i)
        amps.append(amp)
    
    halted = False
    cur_amp = 0
    o = None
    e_output = None
    while not halted:
        if o is None:
            amps[cur_amp].add_input(0)
        else:
            amps[cur_amp].add_input(o)
        
        # run it and get output
        o = amps[cur_amp].output()
        
        # is it halted?
        if amps[cur_amp].halted:
            halted = True
        
        # set up next one
        cur_amp += 1
        if cur_amp > 4:
            cur_amp = 0
            e_output = o
            
    if e_output > bestval:
        bestval = e_output
        bestseq = p
        
                            
print('Max thruster signal',bestval, 'from phase sequence', bestseq)