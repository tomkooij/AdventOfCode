from collections import deque


def take_left(elfs):
    x = []
    for idx in range(0, len(elfs), 2):
        x.append(elfs[idx])
    if len(elfs) % 2:
        x.pop(0)
    return x


def solve_A(elfs):
    while len(elfs) > 1:
        elfs = take_left(elfs)

    return elfs[0]


def solve_B(elfs):
    """
    Remove middle item of list of elfs, rotate 1 step, repeat.
    deque -> O(1) pop and insert
    """

    middle = len(elfs) // 2
    left, right = deque(elfs[:middle]), deque(elfs[middle:])

    while True:
        # remove middle item
        if len(left) > len(right):
            left.pop()
        else:
            right.popleft()

        # if right half is empty --> finished
        if not right:
            return left.pop()

        # rotate
        left.append(right.popleft())
        right.append(left.popleft())


assert solve_A(range(1, 6)) == 3
assert solve_A([1, 2]) == 1
assert solve_B(list(range(1, 6))) == 2

INPUT = 3017957

print(solve_A(range(1, INPUT+1)))
print(solve_B(list(range(1, INPUT+1))))
