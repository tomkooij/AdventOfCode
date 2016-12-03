from collections import deque


move_funcs = deque([lambda x, y, n: (x, y+n),   # north
                    lambda x, y, n: (x+n, y),   # east
                    lambda x, y, n: (x, y-n),   # south
                    lambda x, y, n: (x-n, y)])  # west

direction = {'L': 1, 'R': -1}


def find_second_visit(commands):
    x, y = 0, 0
    visited_locations = {(x, y)}
    for cmd in commands:
        LR = cmd[0]
        n = int(cmd[1:])
        move_funcs.rotate(direction[LR])
        for _ in range(n):
            x, y = move_funcs[0](x, y, 1)
            if (x, y) in visited_locations:
                return (x, y)
            visited_locations.add((x, y))


with open('input/input.txt') as f:
    commands = f.readline().split(', ')
    x, y = find_second_visit(commands)
    print('second time at (%d, %d). '
          '%d blocks away.' % (x, y, abs(x)+abs(y)))
