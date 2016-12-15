import numpy as np

LENGTH = int(1e6)


def parse(line):
    """Disc #1 has 13 positions; at time=0, it is at position 1."""
    Disc, number, _has, n, _pos, _at, _t0, _it, _is, _at, _p, position = line.split()
    assert Disc == 'Disc'
    return list(map(int, (n, position.strip('.'))))


def is_open(t, number_of_slots, start_position):
    return not (t + start_position) % number_of_slots


def solve(dics, length):
    """ very (very) naive brute force search """

    matrix = np.zeros((len(discs), length))

    for idx, disc in enumerate(discs):
        n_slots, start = disc
        matrix[idx] = [is_open(t + idx, n_slots, start) for t in range(length)]

    index_first_all_true_column = np.all(matrix, axis=0).argmax()

    return index_first_all_true_column - 1


with open('input\input15.txt') as f:
    discs = [parse(line.rstrip('\n')) for line in f.readlines()]

print('part A: ', solve(discs, LENGTH))
discs.append((11, 0))
print('part B: ', solve(discs, 11*LENGTH))
