# adventofcode
# day10

from itertools import groupby

INPUT = '1321131112'
TESTCASE = '1'

def LookAndSay(string):
    # from the itertools.groupby() documentation:
    #  https://docs.python.org/2/library/itertools.html#itertools.groupby
    return ''.join(str(len(list(g))) + str(k) for k, g in groupby(string))

line = TESTCASE
for i in range(1,6):
    new = LookAndSay(line)
    print "%s becomes %s" % (line, new)
    line = new
assert line == '312211', 'testcase failure!'

line = INPUT
for i in range(1,51):
    print 'iteration: ', i
    line = LookAndSay(line)
    if i == 40:
        print 'length of result after 40 iterations:', len(line)

print 'length of result after 50 iterations:', len(line)
