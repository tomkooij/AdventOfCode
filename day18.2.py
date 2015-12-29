# adventofcode.com
# day18

from copy import deepcopy

INPUT = ('input/input18', 100)
TESTCASE = ('input/test18', 4)

ON = '#'
OFF = '.'

def pretty_print(lights):
    for l in lights:
        print ''.join(l).rstrip('\n')


def count(lights):
    return sum([l.count('#') for l in lights])


def get_neighbours(lights, x, y):
    neighbours = []
    xmax = ymax = len(lights)
    for i in range(max(y-1, 0), min(y+2, ymax)):
        for j in range(max(x-1,0), min(x+2, xmax)):
            neighbours.append((i,j))
    if (y,x) in neighbours:
        neighbours.remove((y,x))
    return neighbours


def count_neighbours(lights, x, y):
    n = get_neighbours(lights, x, y)
    return count([lights[y][x] for y,x in n])


FILENAME, STEPS = INPUT

if __name__ == '__main__':
    with open(FILENAME) as f:
        lights = map(list, f.read().splitlines())

    for _ in range(STEPS+1):

        length = len(lights)-1
        lights[0][0] = ON
        lights[0][length] = ON
        lights[length][0] = ON
        lights[length][length] = ON

        old_lights = deepcopy(lights)

        pretty_print(lights)
        print count(lights)

        for y in range(0, len(lights)):
            for x in range(0, len(lights)):
                #print y, x, count_neighbours(lights, x, y)
                if old_lights[y][x] == ON:
                    if not count_neighbours(old_lights, x, y) in [2, 3]:
                        lights[y][x] = OFF
                elif old_lights[y][x] == OFF:
                    if count_neighbours(old_lights, x, y) == 3:
                        lights[y][x] = ON
                else:
                    assert False, 'lp0 on fire! %d %d %c' % (x, y, lights[y][x])
