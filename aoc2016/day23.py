# adventofcode assembunny
# day 23 2016 -> day 12 2016 -> day 23 2015
from collections import defaultdict


def run(instructions, **kwargs):

    def int_or_reg(register):
        try:
            return int(register)
        except ValueError:
            return regs[register]

    def toggle(instruction):
        opcode, *rest = instruction
        if opcode == 'inc':
            opcode = 'dec'
        elif opcode == 'dec' or opcode == 'tgl':
            opcode = 'inc'
        elif opcode == 'jnz':
            opcode = 'cpy'
        elif opcode == 'cpy':
            opcode = 'jnz'
        return [opcode, *rest]

    #assert toggle(['tgl', 'a']) == ['inc', 'a']
    #assert toggle(['cpy',  '1',  'a']) == ['jnz', '1', 'a']

    regs = defaultdict(int)
    output = []
    for key, value in kwargs.items():
        regs[key] = value


    while regs['ip'] < len(instructions):

        opcode, *rest = instructions[regs['ip']]
        #print('evaluate: ', regs['ip'], opcode, rest)
        if opcode == 'tgl':
            idx = int_or_reg(rest[0])
            try:
                instructions[regs['ip']+idx] =\
                                toggle(instructions[regs['ip']+idx])
            except IndexError:
                pass
        elif opcode == 'cpy':
            register = rest[1]
            value = rest[0]
            regs[register] = int_or_reg(value)
        elif opcode == 'inc':
            register = rest[0]
            regs[register] += 1
        elif opcode == 'dec':
            register = rest[0]
            regs[register] -= 1
        elif opcode == 'jnz':
            register = rest[0]
            offset = rest[1]
            zero = int_or_reg(register)
            if zero:
                regs['ip'] += int_or_reg(offset) - 1
        elif opcode == 'add':
            register = rest[1]
            value = rest[0]
            regs[register] += int_or_reg(value)
        elif opcode == 'mul':
            register = rest[1]
            value = rest[0]
            regs[register] *= int_or_reg(value)
        else:
            assert False, 'unknown instruction.'

        regs['ip'] += 1

    return regs['a']


with open('input\input23.txt') as f:
    instructions = [line.rstrip('\n').split() for line in f.readlines()]
    print('part A: ', run(instructions, a=7))


with open('input\input23-optimised.txt') as f:
    instructions = [line.rstrip('\n').split() for line in f.readlines()]
    print('part B: ', run(instructions, a=12))
