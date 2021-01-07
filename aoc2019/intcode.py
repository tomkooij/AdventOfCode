from collections import defaultdict

WAITING = -1
HALTED = 0
RUNNING = 1
AWAIT_INPUT = 2


class IntCode(object):

    opcodes = {1: 'ADD',
     2: 'MUL',
     3: 'INPUT',
     4: 'OUTPUT',
     5: 'JNZ',
     6: 'JZ',
     7: 'STORE_LESS',
     8: 'STORE_EQ',
     9: 'SET_REL',
     99: 'HALT'} 
    
    
    def __init__(self, program, input=None, debug=False, verbose=True):
        self.state = WAITING
        self.ip = 0
        self.relative_base = 0      
        self.output = []
        self.mem = defaultdict(int)
        for idx, instruction in enumerate(program):
            self.mem[idx] = instruction
        self.input = input
        self.debug = debug
        self.verbose = verbose
    
    def get_opcode(self):
        self.ip += 1
        instruction = self.mem[self.ip]
        opcode = instruction % 100
        A = instruction % 100000 // 10000
        B = instruction % 10000 // 1000
        C = instruction % 1000 // 100
        self.modes = [A, B, C]
        if self.debug:
            print(f'{self.ip} {instruction} {self.opcodes[opcode]} [{self.mem[self.ip+1]} {self.mem[self.ip+2]} {self.mem[self.ip+3]}]')
        
        return opcode
    
    def load(self):
        self.ip += 1
        value = self.mem[self.ip]
        mode = self.modes.pop()
        if mode == 0:
            addr = value
        elif mode == 1:
            return value
        elif mode == 2:
            addr = value + self.relative_base
        else:
            assert False, f'wrong mode for load: {mode}'
        
        retval = self.mem[addr]
        
        if self.debug:
            print(f'load: [{addr}] {retval}')        
        
        return retval
    
    def store(self, value):
        self.ip += 1
        mode = self.modes.pop()
        
        if mode == 0:
            addr = self.mem[self.ip]
        elif mode == 2:
            addr = self.mem[self.ip] + self.relative_base
        else:
            assert False, f'wrong mode for store: {mode}'
           
        if self.debug:
            print(f'store: {[addr]} {value}')
        
        self.mem[addr] = value
        
    def run(self):
        self.ip -= 1
        self.state = RUNNING
        while self.state == RUNNING:
            self.state = self.step()
        return self.state
    
    def step(self):
        """single step 1 instruction"""
        opcode = self.get_opcode()
        if opcode == 1:
            self.store(self.load() + self.load())
        elif opcode == 2:
            self.store(self.load() * self.load())
        elif opcode == 3:
            try:
                val = self.input.pop(0)
            except IndexError:
                if self.verbose:
                    print('Waiting for input')
                return AWAIT_INPUT
            #print(f'read: {val}')
            self.store(val)  
        elif opcode == 4:
            output = self.load()
            if self.debug:
                print(f'>>>>>>>>>>>>>>>>>>> output: {output}')
            self.output.append(output)
        elif opcode == 5:  # jmp if true
            if self.load():
                self.ip = self.load() - 1
            else:
                self.ip += 1
        elif opcode == 6:  # jmp if false
            if not self.load():
                self.ip = self.load() - 1
            else:
                self.ip += 1
        elif opcode == 7:  # less than
            val = 1 if self.load() < self.load() else 0
            self.store(val)
        elif opcode == 8:  # equal
            val = 1 if self.load() == self.load() else 0
            self.store(val) 
        elif opcode == 9:
            self.relative_base += self.load()
            if self.debug:
                print(f'relativate base: {self.relative_base}')
        elif opcode == 99:
            return HALTED
        else:
            assert False, f'fail @ ip={self.ip}'
        
        return RUNNING
    
    def pop_output(self):
        return self.output.pop()
    
    def get_output(self):
        return self.output
        
    

if __name__ == '__main__':
    testcase = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    i = IntCode(testcase, input=[], debug=False)
    i.run()
    print(i.output)