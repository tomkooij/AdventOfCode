import sys
from collections import deque

x, y = 0, 0

move_funcs = deque([lambda x, y, n: (x, y+n),   # north
                    lambda x, y, n: (x+n, y),   # east
                    lambda x, y, n: (x, y-n),   # south
                    lambda x, y, n: (x-n, y)])  # west

direction = {'L' : 1, 'R': -1}

visited_locations = {(x, y)}

with open('input/input.txt') as f:
    for cmd in f.readline().split(', '):
        LR = cmd[0]
        n = int(cmd[1:])
        move_funcs.rotate(direction[LR])
        for _ in range(n):
            x, y = move_funcs[0](x, y, 1)
            if (x, y) in visited_locations:
                print('second time at (%d, %d). '
                      '%d blocks away.' % (x, y, abs(x)+abs(y)))
                sys.exit()
            visited_locations.add((x, y))

print('finished at (%d, %d). %d blocks away.' % (x, y, abs(x)+abs(y)))
