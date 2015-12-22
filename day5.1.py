#adventofcode.com
#day5.1

INPUTFILE = 'input/input5'

VOWELS = 'aeiou'
FORBIDDEN = ['ab', 'cd', 'pq', 'xy']

TESTCASES = ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']


def is_nice(string):

    # at least 3 vowels:
    number_of_vowels = 0
    for v in VOWELS:
        number_of_vowels += string.count(v)

    doubles = False

    for i in range(len(string)-1):
        if string[i]==string[i+1]:
            doubles = True

    for illegal in FORBIDDEN:
        if string.find(illegal) != -1:
            return False

    return number_of_vowels >= 3 and doubles


for testcase in TESTCASES:
    print testcase, is_nice(testcase)

with open(INPUTFILE) as f:
    lines = f.readlines()

    count = 0
    for line in lines:
        if is_nice(line):
            count += 1
    print "%d nice strings in %s" % (count, INPUTFILE)
