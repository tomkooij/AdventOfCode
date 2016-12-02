
go = {'U': lambda x, y: (x, y+1),
      'L': lambda x, y: (x-1, y),
      'D': lambda x, y: (x, y-1),
      'R': lambda x, y: (x+1, y)}

# keypad:
#    1
#  2 3 4
#5 6 7 8 9
#  A B C
#    D
keypad_map = {( 2,  0): '1',
              ( 1, -1): '2',
              ( 1,  0): '3',
              ( 1,  1): '4',
              ( 0, -2): '5',
              ( 0, -1): '6',
              ( 0,  0): '7',
              ( 0,  1): '8',
              ( 0,  2): '9',
              (-1, -1): 'A',
              (-1,  0): 'B',
              (-1,  1): 'C',
              (-2,  0): 'D'}

x, y = -2, 0  # keypad '5' X, Y ANDERSOM!!
number = '5'
key = ''

with open('input/input2.txt') as f:
    for line in f.readlines():
        for cmd in line.rstrip('\n'):
            x1, y1 = go[cmd](x, y)
            try:
                number = keypad_map[(y1, x1)]
                x, y = x1, y1
            except KeyError:
                pass
        key += number
print(key)
