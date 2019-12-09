class Param:
    def __init__(self, mode, val, mem):
        self.mode = int(mode)
        self.adr = val
        self.mem = mem

    def read(self):
        if self.mode == 0: # position mode
            return self.mem[self.adr]
        if self.mode == 1: # immediate mode
            return self.adr
        raise ValueError('Invalid parameter.', self.mode, self.adr)

    def write(self, val):
        if self.mode == 0:
            self.mem[self.adr] = val
        if self.mode == 1:
            raise ValueError('Cannot write to', self.adr)

class IntCode:

    def __init__(self):
        self.halted = False
        self.ip = 0
        self.mem = []
        self.inputs = []
        
    def add_input(self, input):
        self.inputs.append(input)

    def mem_empty(self, size):
        self.mem = [-1 for x in range(size)]

    def mem_init(self, vals):
        self.mem = vals.copy()

    def mem_set(self, adr, val):
        self.mem[adr] = val
        
    def step(self):
        opcode = str(self.mem[self.ip]).rjust(5, '0')
        
        # HALT
        if opcode[3:] == '99':
            self.halted = True
            return
        
        # ADD
        if opcode[-1] == '1':
            p1 = Param(opcode[2], self.mem[self.ip+1], self.mem)
            p2 = Param(opcode[1], self.mem[self.ip+2], self.mem)
            ds = Param(opcode[0], self.mem[self.ip+3], self.mem)
            ds.write(p1.read() + p2.read())
            self.ip += 4
            return
            
        # MULTIPLY
        if opcode[-1] == '2':
            p1 = Param(opcode[2], self.mem[self.ip+1], self.mem)
            p2 = Param(opcode[1], self.mem[self.ip+2], self.mem)
            ds = Param(opcode[0], self.mem[self.ip+3], self.mem)
            ds.write(p1.read() * p2.read())
            self.ip += 4
            return
        
        # INPUT
        if opcode[-1] == '3':
            ds = Param(opcode[2], self.mem[self.ip+1], self.mem)
            ds.write(self.inputs.pop())
            self.ip += 2
            return
            
        # OUTPUT
        if opcode[-1] == '4':
            p1 = Param(opcode[2], self.mem[self.ip+1], self.mem)
            print(p1.read())
            self.ip += 2
            return
        
        # JUMP IF TRUE
        if opcode[-1] == '5':
            p1 = Param(opcode[2], self.mem[self.ip+1], self.mem)
            p2 = Param(opcode[1], self.mem[self.ip+2], self.mem)
            if p1.read() != 0:
                self.ip = p2.read()
                return
            self.ip += 3
            return
        
        # JUMP IF FALSE
        if opcode[-1] == '6':
            p1 = Param(opcode[2], self.mem[self.ip+1], self.mem)
            p2 = Param(opcode[1], self.mem[self.ip+2], self.mem)
            if p1.read() == 0:
                self.ip = p2.read()
                return
            self.ip += 3
            return
        
        # LESS THAN
        if opcode[-1] == '7':
            p1 = Param(opcode[2], self.mem[self.ip+1], self.mem)
            p2 = Param(opcode[1], self.mem[self.ip+2], self.mem)
            ds = Param(opcode[0], self.mem[self.ip+3], self.mem)
            if p1.read() < p2.read():
                ds.write(1)
            else:
                ds.write(0)
            self.ip += 4
            return
        
        # EQUALS
        if opcode[-1] == '8':
            p1 = Param(opcode[2], self.mem[self.ip+1], self.mem)
            p2 = Param(opcode[1], self.mem[self.ip+2], self.mem)
            ds = Param(opcode[0], self.mem[self.ip+3], self.mem)
            if p1.read() == p2.read():
                ds.write(1)
            else:
                ds.write(0)
            self.ip += 4
            return
        
        raise ValueError('Cannot parse instruction', opcode[3:],  self.mem[self.ip:self.ip + 4])

    def run(self):
        while not self.halted:
            self.step()
            
    def result(self):
        return self.mem[0]