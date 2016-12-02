# adventofcode.com
# day19

from collections import defaultdict

INPUTFILE = 'input/input19'

TEST = False
TESTCASE = ('HOH', ['H => HO\n', 'H => OH\n', 'O => HH\n'], ['OHOH', 'HOOH', 'HHHH', 'HOHO'])

def find_idx(string, substring):
    """ iterator that returns the index of the next occurence of substring
        wrapper around string.find() """
    idx = string.find(substring)
    while idx != -1:
        yield idx
        idx = string.find(substring, idx+1)

def replace_in_string(string, length, substring, idx):
    """ overwrite only length chars in replacement! """
    return string[:idx]+substring+string[idx+length:]

if __name__ == '__main__':

    subs = defaultdict(list)

    if TEST:
        inputstring = TESTCASE[0]
        lines = TESTCASE[1]
        test = TESTCASE[2]
    else:
        with open(INPUTFILE, 'r') as f:
            lines = f.readlines()
        inputstring = lines.pop()
        test = False

    for line in lines:
        if line != '\n':
            f, t = line.rstrip('\n').split(' => ')
            subs[f].append(t)

    solution = []
    for key, sublist in subs.items():
        for sub in sublist:
            for idx in find_idx(inputstring, key):
                solution.append(replace_in_string(inputstring, len(key), sub, idx))

    print "length : ", len(set(solution))

    if test:
        assert set(test) == set(solution), 'Testcase failure!'

    # part B
    # Cheated! #Atoms - 2*(#Rn) - 2*(#Y) - 1
    # https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju
    print 'part B'
    print sum(map(str.isupper,inputstring)) - 2*inputstring.count('Rn') - 2*inputstring.count('Y') - 1
