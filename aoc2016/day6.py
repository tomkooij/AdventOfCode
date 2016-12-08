msg_A, msg_B = '', ''

with open('input/input6-test.txt') as f:
    lines = f.readlines()
    for column in zip(*lines):
        frequencies = sorted(list({(column.count(char), char) for char in
                                                                  column}))
        msg_A += frequencies[-1][1]
        msg_B += frequencies[0][1]

print(msg_A, msg_B)
