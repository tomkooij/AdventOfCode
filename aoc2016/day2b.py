next_position = {'U': lambda x, y: (x, y+1),
                 'L': lambda x, y: (x-1, y),
                 'D': lambda x, y: (x, y-1),
                 'R': lambda x, y: (x+1, y)}

keypad = ['..1..',
          '.234.',
          '56789',
          '.ABC.',
          '..D..']

keypad_map = {}
for x in range(5):
    for y in range(5):
        ch = keypad[4-y][x]
        if ch != '.':
            keypad_map[(x, y)] = ch

x, y = 0, 2
number = keypad_map[(x, y)]
assert number == '5'
key = ''

with open('input/input2.txt') as f:
    for line in f.readlines():
        for move in line.rstrip('\n'):
            try:
                number = keypad_map[next_position[move](x, y)]
                x, y = next_position[move](x, y)
            except KeyError:
                pass
        key += number
print(key)
