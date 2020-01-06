import sys
from intcode import *

m = [int(l) for l in sys.stdin.readline().split(',')]

ic = IntCode()
ic.mem_init(m)
ic.add_input(2)
while not ic.halted:
    print(ic.output())