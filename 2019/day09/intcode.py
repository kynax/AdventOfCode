class Param:
    def __init__(self, mode, val, intcode):
        self.mode = int(mode)
        self.adr = val
        self.intcode = intcode

    def read(self):
        if self.mode == 0: # position mode
            if self.adr not in self.intcode.mem:
                return 0
            return self.intcode.mem[self.adr]
        if self.mode == 1: # immediate mode
            return self.adr
        if self.mode == 2: # relative mode
            if self.intcode.rel_adr + self.adr not in self.intcode.mem:
                return 0
            return self.intcode.mem[self.intcode.rel_adr + self.adr]
        raise ValueError('Invalid parameter.', self.mode, self.adr)

    def write(self, val):
        if self.mode == 0:
            self.intcode.mem[self.adr] = val
        if self.mode == 2:
            self.intcode.mem[self.intcode.rel_adr + self.adr] = val
        if self.mode == 1:
            raise ValueError('Cannot write to', self.adr)

class IntCode:

    def __init__(self):
        self.halted = False
        self.ip = 0
        self.mem = {}
        self.inputs = []
        self.rel_adr = 0
        
    def add_input(self, input):
        self.inputs.append(input)

    def mem_empty(self, size):
        self.mem = [-1 for x in range(size)]

    def mem_init(self, vals):
        for i in range(len(vals)):
            self.mem[i] = vals[i]

    def mem_set(self, adr, val):
        self.mem[adr] = val
        
    def output(self):
        while True:
            r = self.step()
            if self.halted == True or r is not None:
                return r
        
        
    def step(self):
        opcode = str(self.mem[self.ip]).rjust(5, '0')
        
        # HALT
        if opcode[3:] == '99':
            self.halted = True
            return None
        
        # ADD
        if opcode[-1] == '1':
            p1 = Param(opcode[2], self.mem[self.ip+1], self)
            p2 = Param(opcode[1], self.mem[self.ip+2], self)
            ds = Param(opcode[0], self.mem[self.ip+3], self)
            ds.write(p1.read() + p2.read())
            self.ip += 4
            return
            
        # MULTIPLY
        if opcode[-1] == '2':
            p1 = Param(opcode[2], self.mem[self.ip+1], self)
            p2 = Param(opcode[1], self.mem[self.ip+2], self)
            ds = Param(opcode[0], self.mem[self.ip+3], self)
            ds.write(p1.read() * p2.read())
            self.ip += 4
            return
        
        # INPUT
        if opcode[-1] == '3':
            ds = Param(opcode[2], self.mem[self.ip+1], self)
            ds.write(self.inputs.pop(0))
            self.ip += 2
            return
            
        # OUTPUT
        if opcode[-1] == '4':
            p1 = Param(opcode[2], self.mem[self.ip+1], self)
            #print(p1.read())
            self.ip += 2
            return p1.read()
        
        # JUMP IF TRUE
        if opcode[-1] == '5':
            p1 = Param(opcode[2], self.mem[self.ip+1], self)
            p2 = Param(opcode[1], self.mem[self.ip+2], self)
            if p1.read() != 0:
                self.ip = p2.read()
                return
            self.ip += 3
            return
        
        # JUMP IF FALSE
        if opcode[-1] == '6':
            p1 = Param(opcode[2], self.mem[self.ip+1], self)
            p2 = Param(opcode[1], self.mem[self.ip+2], self)
            if p1.read() == 0:
                self.ip = p2.read()
                return
            self.ip += 3
            return
        
        # LESS THAN
        if opcode[-1] == '7':
            p1 = Param(opcode[2], self.mem[self.ip+1], self)
            p2 = Param(opcode[1], self.mem[self.ip+2], self)
            ds = Param(opcode[0], self.mem[self.ip+3], self)
            if p1.read() < p2.read():
                ds.write(1)
            else:
                ds.write(0)
            self.ip += 4
            return
        
        # EQUALS
        if opcode[-1] == '8':
            p1 = Param(opcode[2], self.mem[self.ip+1], self)
            p2 = Param(opcode[1], self.mem[self.ip+2], self)
            ds = Param(opcode[0], self.mem[self.ip+3], self)
            if p1.read() == p2.read():
                ds.write(1)
            else:
                ds.write(0)
            self.ip += 4
            return
        
        # RELATIVE BASE ADJUST
        if opcode[-1] == '9':
            p1 = Param(opcode[2], self.mem[self.ip+1], self)
            self.rel_adr += p1.read()
            self.ip += 2
            return
        
        raise ValueError('Cannot parse instruction', opcode,  self.mem[self.ip], self.mem[self.ip+1], self.mem[self.ip+2], self.mem[self.ip+3], self.mem[self.ip + 4])

    def run(self):
        while not self.halted:
            self.step()
            
    def result(self):
        return self.mem[0]