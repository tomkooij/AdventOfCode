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


with open('input\input22.txt') as f:
    lines = f.readlines()[2:]
    nodes = list(map(parse, lines))

    n = 0
    for a, b in permutations(nodes,2):
        if a[3] > 0:
            if b[4] >= a[3]:
                n += 1
    print(n)
