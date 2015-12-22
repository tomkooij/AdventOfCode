#adventofcode.com
#day5.1

import string

INPUTFILE = 'input/input5'

TESTCASES = ['aaaa', 'qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy', 'dvszwmarrgswjxmb']


def is_nice(string):

    found_doubles = False
    for idx in range(len(string)-2):
        s = string[idx:idx+2]
        second = string.find(s, idx+2)
        if second > idx+1:
            found_doubles = True

    found_singles = False
    for idx, s in enumerate(string):
        second = string.find(s, idx+2)
        if second == idx+2:
            found_singles = True

    return found_doubles and found_singles


for testcase in TESTCASES:
    print testcase, is_nice(testcase)


with open(INPUTFILE) as f:
    lines = f.readlines()

    count = 0
    for line in lines:
        if is_nice(line):
            count += 1
    print "%d nice strings in %s" % (count, INPUTFILE)
