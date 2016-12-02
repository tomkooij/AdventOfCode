from collections import deque

x, y = 0, 0

directions = deque([lambda x, y, n: (x, y+n),   # north
                    lambda x, y, n: (x+n, y),   # east
                    lambda x, y, n: (x, y-n),   # south
                    lambda x, y, n: (x-n, y)])  # west

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
        x, y = directions[0](x, y, n)

print('finished at (%d, %d). %d blocks away.' % (x, y, abs(x)+abs(y)))
