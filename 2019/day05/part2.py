import sys
from intcode import *

m = [int(l) for l in sys.stdin.readline().split(',')]

c = IntCode()
c.mem_init(m)
c.add_input(5)
c.run()