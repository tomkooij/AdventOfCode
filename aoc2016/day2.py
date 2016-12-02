
go = {'U': lambda x, y: (x, y+1),
      'L': lambda x, y: (x-1, y),
      'D': lambda x, y: (x, y-1),
      'R': lambda x, y: (x+1, y)}

# keypad:
# 1 2 3
# 4 5 6
# 7 8 9
#
# (0, 0) -> 7
# (1, 1) -> 5
# (2, 2) -> 3
keypad_map = {}
coords = [(a, b) for a in range(2, -1, -1) for b in range(3)]
for number, keypad in enumerate(coords, 1):
        keypad_map[keypad] = number


x, y = 1, 1  # keypad '5'
key = ''

with open('input/input2.txt') as f:
    for line in f.readlines():
        for cmd in line.rstrip('\n'):
            x1, y1 = go[cmd](x, y)
            try:
                number = str(keypad_map[(y1, x1)])
                x, y = x1, y1
            except KeyError:
                pass
        key += number
print(key)
