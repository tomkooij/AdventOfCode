# adventofcode
# day 13

from collections import defaultdict

INPUTFILE = 'input/input13'
TESTINPUTFILE = 'input/test13'
TESTCASE = ['David', 'Alice', 'Bob', 'Carol']


def happiness(seats, potential):

    total = 0
    for i in range(len(seats)):
        left = i
        right = i+1 if i+1 < len(seats) else 0
        total += potential[seats[left]][seats[right]]
        total += potential[seats[right]][seats[left]]
    return total


def parse(infile):
    with open(infile) as f:
        lines = f.readlines()

        names = []
        potential = defaultdict(dict)

        for line in lines:
            s = line.split()
            assert s[4] == 'happiness', 'lp0 on fire!'
            name1 = s[0]
            gain = int(s[3])
            if s[2] == 'lose':
                gain = -gain
            name2 = s[10][:-1]  # remove last .

            potential[name1][name2] = gain
            names.append(name1)

    return list(set(names)), potential


if __name__ == '__main__':
    names, testpotential = parse(TESTINPUTFILE)
    names = TESTCASE
    score = happiness(TESTCASE, testpotential)
    print names, score
    assert score == 330, 'testcase fails!'
