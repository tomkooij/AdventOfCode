import numpy as np


def parse(line):
    """Disc #1 has 13 positions; at time=0, it is at position 1."""
    Disc, number, _has, n, _pos, _at, _t0, _it, _is, _at, _p, position = line.split()
    assert Disc == 'Disc'
    return list(map(int, (n, position.strip('.'))))


def is_open(t, number_of_slots, start_position):
    return not (t + start_position) % number_of_slots


def solve(dics):
    """ very (very) naive brute force search """

    length = 1000  # search 1000 columns at a time

    matrix = np.zeros((len(discs), length))
    t_offset = 0
    while True:
        for idx, disc in enumerate(discs):
            matrix[idx] = [is_open(t + idx + t_offset, *disc) for t in range(length)]

        index_first_all_true_column = np.all(matrix, axis=0).argmax()

        if index_first_all_true_column > 0 or np.all(matrix[:, 0]):
            return t_offset + index_first_all_true_column - 1

        t_offset += length


with open('input\input15.txt') as f:
    discs = [parse(line.rstrip('\n')) for line in f.readlines()]

print('part A: ', solve(discs))
discs.append((11, 0))
print('part B: ', solve(discs))
