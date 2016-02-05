#adventofcode.com
#day7.1
#
# Algorithm: Repeatedly process the list of gates. Removing processed gates
#  logic was added "on the fly" -->
#     "number AND gate -> gate" is implemented, but "number OR gate -> gate" is not.

import functools

INPUTFILE = 'input/input7'
#INPUTFILE = 'input/test7'

# note that this decorator ignores **kwargs
def memoize(obj):
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

def assign(f, in_a, in_b, out):
    signal[out] = [f, in_a, in_b]

computing = []

#@memoize
def eval(key):
    if key is None:
        return key
    if key.isdigit():
        return int(key)
    if signal[key][0] == 'int':
        return int(signal[key][1])

    return signal[key][0](eval(signal[key][1]),eval(signal[key][2]))


def parse(line):
    s = line.split()
    if len(s) == 5:
        a, op, b, arrow, out = s
        assert arrow == '->'
        if op == 'AND':
            f = AND
        elif op == 'OR':
            f = OR
        elif op == 'RSHIFT':
            f = RSHIFT
        elif op == 'LSHIFT':
            f = LSHIFT
        else:
            print  "unknown input len 5: ", s
            assert False
    elif len(s) == 4:
        op, a, arrow, out = s
        b = None
        f = NOT
        assert arrow == '->'
    elif len(s) == 3:
        a, arrow, out = s
        assert arrow == '->'
        b = None
        if a.isdigit():
            a = int(a)
            f = 'int'
        else:
            f = COPY
    else:
        print  "unknown input: ", s
        assert False
    assign(f, a, b, out)

signal = {}

with open(INPUTFILE) as f:
    for line in f.readlines():
        parse(line)

print "result: a = ", eval('a')
