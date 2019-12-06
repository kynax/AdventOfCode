class IntCode:

    def __init__(self):
        self.halted = False
        self.ip = 0
        self.mem = []

    def mem_empty(self, size):
        self.mem = [-1 for x in range(size)]

    def mem_init(self, vals):
        self.mem = vals.copy()

    def mem_set(self, adr, val):
        self.mem[adr] = val

    def step(self):

        if self.mem[self.ip] == 99:
            self.halted = True

        elif self.mem[self.ip] == 1:
            self.mem[self.mem[self.ip+3]] = self.mem[self.mem[self.ip+1]] + self.mem[self.mem[self.ip+2]]
            self.ip = self.ip + 4

        elif self.mem[self.ip] == 2:
            self.mem[self.mem[self.ip+3]] = self.mem[self.mem[self.ip+1]] * self.mem[self.mem[self.ip+2]]
            self.ip = self.ip + 4

        else:
            self.halted = True
            #raise ValueError('Unknown opcode', self.mem[self.ip:])

    def run(self):
        while not self.halted:
            self.step()
            
    def result(self):
        return self.mem[0]