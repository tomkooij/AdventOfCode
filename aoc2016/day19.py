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
        #print(elfs)
        elfs = take_left(elfs)

    return elfs[0]


def solve_B(elfs):
    middle = len(elfs) // 2
    left, right = deque(elfs[:middle]), deque(elfs[middle:])
    len_left = len(left)
    len_right = len(right)
    while True:
        # remove middle item
        if len(left) > len(right):
            last_elf = left.pop()
        else:
            last_elf = right.popleft()
        #print('removed middle', left, right)

        len_left = len(left)
        len_right = len(right)
        if len_left == 1 and len_right == 0:
            return left.pop()
        # rotate
        left.append(right.popleft())
        right.append(left.popleft())
        #print('after rotate', left, right)

assert solve_A(range(1, 6)) == 3
assert solve_A([1, 2]) == 1
assert solve_B(list(range(1, 6))) == 2

INPUT = 3017957

print(solve_A(range(1, INPUT+1)))
print(solve_B(list(range(1, INPUT+1))))
