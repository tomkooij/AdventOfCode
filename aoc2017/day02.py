import itertools


def evenly(x, y):
    if x == y: return 0
    if x < y:
        x,y = y,x
    if not (x % y): return x // y
    return 0


with open('input/input02.txt') as f:

    rows = [list(map(int, line.split())) for line in f.readlines()]
    print('part a', sum([(max(row) - min(row)) for row in rows]))

    x = 0
    for row in rows:
        x += sum([evenly(i, j) for i,j in itertools.combinations(row, 2)])
    print('part b', x)
