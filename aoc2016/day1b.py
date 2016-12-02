import sys
from collections import deque

x, y = 0, 0

directions = deque([lambda x, y, n: (x, y+n),   # north
                    lambda x, y, n: (x+n, y),   # east
                    lambda x, y, n: (x, y-n),   # south
                    lambda x, y, n: (x-n, y)])  # west

visited_locations = {(x, y)}

with open('input/input.txt') as f:
    for cmd in f.readline().split(', '):
        LR = cmd[0]
        n = int(cmd[1:])
        #print(x, y, 'going', LR, n)
        if LR == 'L':
            directions.rotate(1)
        else:
            directions.rotate(-1)
        #print(directions[0])
        for _ in range(n):
            x, y = directions[0](x, y, 1)
            if (x, y) in visited_locations:
                print('second time at (%d, %d). '
                      '%d blocks away.' % (x, y, abs(x)+abs(y)))
                sys.exit()
            visited_locations.add((x, y))

print('finished at (%d, %d). %d blocks away.' % (x, y, abs(x)+abs(y)))
