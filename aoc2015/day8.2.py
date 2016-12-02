# adventofcode
# day 8.1

INPUTFILE = 'input/input8'
TESTCASES = ['""\n', '"abc"\n', '"aaa\"aaa"\n', '"\x27"\n']

with open(INPUTFILE) as f:
    lines = f.readlines()

    total = 0
    for line in lines:
        code = len(line)-1
        escaped = len(line)+1 + line.count('"') + line.count("\\")

        total += (escaped - code)

    print "answer = ", total
