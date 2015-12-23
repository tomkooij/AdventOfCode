# adventofcode
# day 23

INPUTFILE = 'input/input23'

def evaluate(instruction, regs):

    opcode, register, offset = instruction

    if opcode == 'hlf':
        regs[register] /= 2
        regs['ip'] += 1
    elif opcode == 'tpl':
        regs[register] *= 3
        regs['ip'] += 1
    elif opcode == 'inc':
        regs[register] += 1
        regs['ip'] += 1
    elif opcode == 'jmp':
        regs['ip'] += int(offset)
    elif opcode == 'jie':
        if not regs[register] % 2:
            regs['ip'] += int(offset)
        else:
            regs['ip'] += 1
    elif opcode == 'jio':
        if regs[register] == 1:
            regs['ip'] += int(offset)
        else:
            regs['ip'] += 1
    else:
        assert False, 'unknown instruction.'

    return regs


def parse(infile):
    with open(infile) as f:
        lines = f.readlines()

        instructions = []

        for idx, line in enumerate(lines):
            opcode = register = offset = None
            if ',' in line:
                first, offset = line.split(', ')
                opcode, register = first.split()
            elif line[0:3] == 'jmp':
                opcode, offset = line.split()
            else:
                opcode, register = line.split()

            instructions.append((opcode, register, offset))

    return instructions


if __name__ == '__main__':
    instructions = parse(INPUTFILE)
    regs = {}
    regs['ip'] = 0
    regs['a'] = 0
    regs['b'] = 0
    while regs['ip'] < len(instructions):
        regs = evaluate(instructions[regs['ip']], regs)
    print 'ip: %d a: %d b: %d' % (regs['ip'], regs['a'], regs['b'])
