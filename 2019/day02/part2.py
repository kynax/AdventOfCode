import sys
from intcode import *

m = [int(l) for l in sys.stdin.readline().split(',')]

for verb in range(100):
    for noun in range(100):
        c = IntCode()
        c.mem_init(m)
        c.mem_set(1, noun)
        c.mem_set(2, verb)
        c.run()
        
        if c.result() == 19690720:
            print(100 * noun + verb)
            