#adventofcode.com
#day5.1

import string

INPUTFILE = 'input/input5'

TESTCASES = ['aaaa', 'qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy', 'dvszwmarrgswjxmb']


def int2char(i):
    return string.lowercase[i % 26] * (i/26+1)


# ['aa', 'ab', .. , 'zz']
doubles = []
for i in range(26):
    for j in range(26):
        doubles.append(int2char(i)+int2char(j))


def is_nice(string):

    found = False
    for d in doubles:
        first = string.find(d)
        if first != -1:
            second = string.find(d, first+2)
            if second > first+1:
                found = True

    if found is False:
        return False

    found = False
    for idx, s in enumerate(string):
        second = string.find(s, idx+2)
        if second == idx+2:
            found = True

    if found is False:
        return False

    return True


for testcase in TESTCASES:
    print testcase, is_nice(testcase)


with open(INPUTFILE) as f:
    lines = f.readlines()

    count = 0
    for line in lines:
        if is_nice(line):
            count += 1
    print "%d nice strings in %s" % (count, INPUTFILE)
