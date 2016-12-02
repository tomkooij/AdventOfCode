from collections import deque

x, y = 0, 0

move_funcs = deque([lambda x, y, n: (x, y+n),   # north
                    lambda x, y, n: (x+n, y),   # east
                    lambda x, y, n: (x, y-n),   # south
                    lambda x, y, n: (x-n, y)])  # west

direction = {'L' : 1, 'R': -1}

with open('input/input.txt') as f:
    for cmd in f.readline().split(', '):
        LR = cmd[0]
        n = int(cmd[1:])
        move_funcs.rotate(direction[LR])
        x, y = move_funcs[0](x, y, n)

print('finished at (%d, %d). %d blocks away.' % (x, y, abs(x)+abs(y)))
