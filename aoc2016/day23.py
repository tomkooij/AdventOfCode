# adventofcode
# day 23 2016 -> day 12 2016 -> day 23 2015
from collections import defaultdict

def int_or_reg(register, regs):
    try:
        return int(register)
    except ValueError:
        return regs[register]

def evaluate(instruction, regs):
    opcode, *rest = instruction
    print('evaluate ', instruction)
    if opcode == 'cpy':
        register = rest[1]
        value = rest[0]
        regs[register] = int_or_reg(value, regs)
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
        zero = int_or_reg(register, regs)
        if zero:
            regs['ip'] += int_or_reg(offset, regs)
        else:
            regs['ip'] += 1
    else:
        assert False, 'unknown instruction.'


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

assert toggle(['tgl', 'a']) == ['inc', 'a']
assert toggle(['cpy',  '1',  'a']) == ['jnz', '1', 'a']

def run(*args, **kwargs):
    regs = defaultdict(int)
    for key, value in kwargs.items():
        regs[key] = value

    while regs['ip'] < len(instructions):

        # hack toggle
        opcode, *rest = instructions[regs['ip']]
        if opcode == 'tgl':
            try:
                idx = int(rest[0])
            except ValueError:
                idx = regs[rest[0]]
            print('toggling ', idx, rest)
            try:
                instructions[regs['ip']+idx] =\
                                toggle(instructions[regs['ip']+idx])
            except IndexError:
                print('no such index for toggle', idx)
            regs['ip'] += 1
        else:
            evaluate(instructions[regs['ip']], regs)

    return regs['a']


with open('input\input23-test.txt') as f:
    instructions = [line.rstrip('\n').split() for line in f.readlines()]

print('part A: ', run())
#print('part B: ', run(c=1))
