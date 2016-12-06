passwordA, passwordB = '', ''

with open('input/input6-test.txt') as f:
    lines = f.readlines()
    for column in zip(*lines):
        frequencies = sorted(list({(column.count(char), char) for char in
                                                                  column}))
        passwordA += frequencies[-1][1]
        passwordB += frequencies[0][1]

print(passwordA, passwordB)
