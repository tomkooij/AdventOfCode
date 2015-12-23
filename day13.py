# adventofcode
# day 13

INPUTFILE = 'input/input13'




def parse(infile):
    with open(infile) as f:
        lines = f.readlines()

        potential = []

        for line in lines:
            s = line.split()
            assert s[4] == 'happiness', 'lp0 on fire!'
            name1 = s[0]
            gain = int(s[3])
            if s[2] == 'lose':
                gain = -gain
            name2 = s[10][:-1]  # remove last .

            potential.append((name1, gain, name2))

    return potential


if __name__ == '__main__':
    potential = parse(INPUTFILE)
