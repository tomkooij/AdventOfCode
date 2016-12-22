import numpy as np
from itertools import permutations

def parse(line):
    """/dev/grid/node-x35-y8    88T   71T    17T   80%"""
    node, size, used, avail, perc = line.split()
    _, x, y = node.split('-')
    x = int(x[1:])
    y = int(y[1:])
    used = int(used[:-1])
    size = int(size[:-1])
    avail = int(avail[:-1])
    return x, y, size, used, avail

def partA(nodes):
    n = 0
    for a, b in permutations(nodes,2):
        if a[3] > 0:
            if b[4] >= a[3]:
                n += 1
    return n


with open('input\input22.txt') as f:
    lines = f.readlines()[2:]
    nodes = list(map(parse, lines))


#print('part A', partA(nodes))
nodes = np.array(nodes)
x = nodes[:, 0]
y = nodes[:, 1]
max_x, max_y = max(x), max(y)
xmax = max_x

node = {}
for x, y, size, used, avail in nodes:
    node[(y, x)] = (size, used, avail)

for r in range(max_y+1):
    line = ''
    for c in range(max_x+1):
        try:
            if node[(r, c)][0] > 100:
                char = ' # '
            else:
                char = ' . '
            if node[(r, c)][1] == 0:
                char = ' _ '
                x0 = c
                y0 = r
        except KeyError:
            char = ' E '
        if (r, c) == (0, max_x):
            char = ' G '
        line += char
    print(line)

print('goal = ', node[(0, max_x)])
