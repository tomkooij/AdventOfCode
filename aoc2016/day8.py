import numpy as np

HEIGHT = 6
WIDTH = 50

screen = np.zeros(WIDTH*HEIGHT).reshape(HEIGHT, WIDTH)


def print_screen():
    for r in range(HEIGHT):
        for c in range(WIDTH):
            if screen[r][c]:
                print('#', end='')
            else:
                print(' ', end='')
        print('')


def rect(A, B):
    screen[0:B, 0:A] = 1


def rotate_column(col, n):
    column = screen[:, col]
    screen[:, col] = np.roll(column, n)


def rotate_row(row, n):
    rowarray = screen[row]
    screen[row] = np.roll(rowarray, n)


def parse(line):
    command, *args = line.split()
    if command == 'rect':
        A, B = map(int, args[0].split('x'))
        rect(A, B)
    if command == 'rotate':
        rc = int(args[1].split('=')[-1])
        n = int(args[3])
        if args[0] == 'row':
            rotate_row(rc, n)
        elif args[0] == 'column':
            rotate_column(rc, n)


with open('input/input8.txt') as f:
    for line in f.readlines():
        parse(line)

print(sum(sum(screen)))
print_screen()
