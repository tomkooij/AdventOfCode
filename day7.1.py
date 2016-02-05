#adventofcode.com
#day7.1
#
# Algorithm: Repeatedly process the list of gates. Removing processed gates
#  logic was added "on the fly" -->
#     "number AND gate -> gate" is implemented, but "number OR gate -> gate" is not.

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


def AND(a, b): return a & b
def OR(a, b): return a | b
def RSHIFT(a, b): return a >> b
def LSHIFT(a, b): return a << b
def NOT(a, b): return ~a & 0xffff  # unsigned int!
def COPY(a, b): return a


@memoize
def eval(key):
    """ recursively evaluate a statement from signal dict. Needs memoisation! """
    if key is None:
        return key
    if key.isdigit():
        return int(key)
    if signal[key][0] == 'int':
        return int(signal[key][1])

    # recursively evaluate the arguments [1],[2] then call the function in [0]
    return signal[key][0] ( eval(signal[key][1]), eval(signal[key][2]) )


def parse(line):
    """
    parses lines into list [function, left, right, out]:

    example: parse('x AND y -> z') returns ['AND', x, y, z]
    """
    s = line.split()
    if len(s) == 5:
        # AND, OR, RSHIFT, LSHIFT
        a, op, b, arrow, out = s
        assert arrow == '->'
    elif len(s) == 4:
        # NOT
        op, a, arrow, out = s
        assert arrow == '->'
        b = None
    elif len(s) == 3:
        # Assignment
        a, arrow, out = s
        assert arrow == '->'
        b = None
        if a.isdigit():
            a = int(a)
            op = 'integer'
        else:
            op = 'COPY'
    else:
        print  "unknown input: ", s
        assert False

    return op, a, b, out

op_to_func = {'AND': AND,
             'OR': OR,
             'RSHIFT': RSHIFT,
             'LSHIFT': LSHIFT,
             'NOT': NOT,
             'COPY': COPY,
             'integer': 'int'}

signal = {}

with open(INPUTFILE) as f:
    for line in f.readlines():
        op, a, b, out = parse(line)
        signal[out] = [op_to_func[op], a, b]

print "result: a = ", eval('a')
