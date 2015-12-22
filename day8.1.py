# adventofcode
# day 8.1

INPUTFILE = 'input/input8'
TESTCASES = ['""\n', '"abc"\n', '"aaa\"aaa"\n']

with open(INPUTFILE) as f:
    lines = f.readlines()

    total = 0
    for line in lines:
        code = len(line)-1
        memory = len(line.decode('string_escape'))-3

        total += (code - memory)

    print "answer = ", total
