# adventofcode
# day12

import json

INPUTFILE = 'input/input12'

def process(obj):

    if type(obj) == int:
        return obj

    elif type(obj) == dict:
        if partB and 'red' in obj.values():
            return 0
        return sum(map(process, obj.values()))

    elif type(obj) == list:
        return sum(map(process, obj))

    elif type(obj) == unicode:
        return 0

    else:
        print obj, type(obj)
        assert False, 'lp0 on fire!'


partB = False  # horrible global

with open(INPUTFILE, 'r') as f:
    j = json.loads(f.readline())  # just one line
print 'part A: ', process(j)
partB = True
print 'part B: ', process(j)
