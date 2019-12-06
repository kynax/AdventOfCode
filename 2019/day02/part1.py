import sys
from intcode import *

m = [int(l) for l in sys.stdin.readline().split(',')]

c = IntCode()
c.mem_init(m)
c.mem_set(1, 12)
c.mem_set(2, 2)
c.run()
print(c.result())