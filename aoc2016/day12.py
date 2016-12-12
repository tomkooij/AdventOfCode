# adventofcode
# day 12 2016 -> day 23 2015
from collections import defaultdict


regs = defaultdict(int)
regs['ip'] = 0

def evaluate(instruction):
    opcode, *rest = instruction

    if opcode == 'cpy':
        register = rest[1]
        value = rest[0]
        try:
            regs[register] = int(value)
        except ValueError:
            regs[register] = regs[value]
        regs['ip'] += 1
    elif opcode == 'inc':
        register = rest[0]
        regs[register] += 1
        regs['ip'] += 1
    elif opcode == 'dec':
        register = rest[0]
        regs[register] -= 1
        regs['ip'] += 1
    elif opcode == 'jnz':
        register = rest[0]
        offset = rest[1]
        try:
            zero = int(register)
        except ValueError:
            zero = regs[register]
        if zero:
            regs['ip'] += int(offset)
        else:
            regs['ip'] += 1
    else:
        assert False, 'unknown instruction.'



with open('input\input12.txt') as f:
    instructions = [line.rstrip('\n').split() for line in f.readlines()]
    # regs['c'] = 1   # part B

    while regs['ip'] < len(instructions):
        evaluate(instructions[regs['ip']])

    print ('ip: %d a: %d b: %d' % (regs['ip'], regs['a'], regs['b']))
