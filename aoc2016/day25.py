# adventofcode assembunny
from collections import defaultdict


def run(len_output, **kwargs):

    def int_or_reg(register):
        try:
            return int(register)
        except ValueError:
            return regs[register]

    regs = defaultdict(int)
    output = []
    for key, value in kwargs.items():
        regs[key] = value

    while regs['ip'] < len(instructions):

        opcode, *rest = instructions[regs['ip']]
        #print('evaluate ', instruction)
        if opcode == 'cpy':
            register = rest[1]
            value = rest[0]
            regs[register] = int_or_reg(value)
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
            zero = int_or_reg(register)
            if zero:
                regs['ip'] += int_or_reg(offset)
            else:
                regs['ip'] += 1
        elif opcode == 'out':
            value = int_or_reg(rest[0])
            output.append(value)
            if len(output) >= len_output:
                return output
            regs['ip'] += 1
        else:
            assert False, 'unknown instruction.'

    return regs['a']


with open('input\input25.txt') as f:
    instructions = [line.rstrip('\n').split() for line in f.readlines()]
    print('part A: ')

# stupid brute force
for i in range(1000):
    if not i % 25:
        print(i)
    if run(16, a=i)== 8*[0, 1]:
        print('part A: ', i)
        break
