from collections import defaultdict


def make_op(reg_name, value):
    """return a function that modifies a registers"""
    def op(registers):
        registers[reg_name] += value
    return op


def parse(row):
    """parse a row, return a function and a condition to eval()"""

    opreg, op, opval, _if, condreg, condop, condval = row.split() 
 
    val = int(opval)
    if op == 'dec':
        val *= -1
    inst = make_op(opreg, val)
    
    condition = 'regs[\''+condreg+'\']'+condop+condval
    return (inst, condition)


with open('input\input08.txt') as f:
    instructions = [parse(row.strip()) for row in f.readlines()]
    regs = defaultdict(lambda: 0)
    max_value = 0
    for instruction, condition in instructions:
        if eval(condition):
            instruction(regs)
            max_value = max(max_value, max(regs.values()))

    print('part a:', max(regs.values()))
    print('part b:', max_value)