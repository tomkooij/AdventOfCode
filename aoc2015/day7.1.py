#adventofcode.com
#day7.1
#
# recursively evaluate wires.

import functools

INPUTFILE = 'input/input7'
#INPUTFILE = 'input/test7'


def memoize(obj):
    """
    memoiser decorator
    https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
    """
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer


@memoize
def eval(key):
    """ recursively evaluate a statement from signal dict. Needs memoisation! """

    def AND(a, b): return a & b
    def OR(a, b): return a | b
    def RSHIFT(a, b): return a >> b
    def LSHIFT(a, b): return a << b
    def NOT(a, b): return ~a & 0xffff  # unsigned int!
    def COPY(a, b): return a

    operator_to_function = {'AND': AND,
                            'OR': OR,
                            'RSHIFT': RSHIFT,
                            'LSHIFT': LSHIFT,
                            'NOT': NOT,
                            'COPY': COPY}

    if key is None:
        return key
    if str(key).isdigit():
        return int(key)

    operator, left, right = signal[key]

    return operator_to_function[operator] ( eval(left), eval(right) )


def parse(line):
    """
    parses lines into list [function, left, right, out]:

    example: parse('x AND y -> z') returns ['AND', x, y, z]
    """
    left, out = line.split(' -> ')
    left = left.split()
    if len(left) == 3:
        # AND, OR, RSHIFT, LSHIFT
        a, op, b = left
    elif len(left) == 2:
        # NOT
        op, a = left
        b = None
    else:
        # Assignment
        a = left[0]
        b = None
        if a.isdigit():
            a = int(a)
        op = 'COPY'

    return op, a, b, out


signal = {}

with open(INPUTFILE) as f:
    for line in f.readlines():
        operator, left, right, out = parse(line.strip('\n'))
        signal[out] = [operator, left, right]

print "result: a = ", eval('a')
