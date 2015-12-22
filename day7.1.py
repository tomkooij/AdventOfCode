#adventofcode.com
#day7.1
#
# Algorithm: Repeatedly process the list of gates. Removing processed gates
#  logic was added "on the fly" -->
#     "number AND gate -> gate" is implemented, but "number OR gate -> gate" is not.

INPUTFILE = 'input/input7'
#INPUTFILE = 'input/test7'


SIZE = 1000

lights = SIZE*SIZE*[0]

def AND(a, b): return a & b
def OR(a, b): return a | b
def RSHIFT(a, b): return a >> b
def LSHIFT(a, b): return a << b
def NOT(a, b): return ~a & 0xffff  # unsigned int!

def do(f, in_a, in_b, out):
    try:
        a = signal[in_a]
    except KeyError:
        a = int(in_a)
    try:
        b = signal[in_b]
    except KeyError:
        b = int(in_b)

    signal[out] = f(a, b)

signal = {}

with open(INPUTFILE) as f:
    lines = f.readlines()

    last = len(lines)+1
    while len(lines) > 0:
        print "lines to go", len(lines)
        if len(lines) == last:
            print "fail!", lines
            break
        last = len(lines)

        for idx,line in enumerate(lines):
            s = line.split()
            if s[1] == 'AND':
                assert s[3] == '->'
                if (s[0].isdigit()) and (s[2] in signal):
                    lines.pop(idx)
                    do(AND, s[0], s[2], s[4])
                if (s[0] in signal) and (s[2] in signal):
                    lines.pop(idx)
                    do(AND, s[0], s[2], s[4])
            elif s[1] == 'OR':
                assert s[3] == '->'
                if (s[0] in signal) and (s[2] in signal):
                    lines.pop(idx)
                    do(OR, s[0], s[2], s[4])
            elif s[1] == 'RSHIFT':
                assert s[3] == '->'
                if (s[0] in signal):
                    lines.pop(idx)
                    do(RSHIFT, s[0], s[2], s[4])
            elif s[1] == 'LSHIFT':
                assert s[3] == '->'
                if (s[0] in signal):
                    lines.pop(idx)
                    do(LSHIFT, s[0], s[2], s[4])
            elif s[0] == 'NOT':
                assert s[2] == '->'
                if (s[1] in signal):
                    lines.pop(idx)
                    do(NOT, s[1], 0, s[3])
            elif s[1] == '->':
                if s[0].isdigit():
                    signal[s[2]] = int(s[0])
                    lines.pop(idx)
                elif(s[0] in signal):
                    signal[s[2]] = signal[s[0]]
                    lines.pop(idx)
            else:
                print "skipping unknown input: ", s

    print "result: a = ", signal['a']
