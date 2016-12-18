def is_trap(left, center, right):
    if left and center and not right:
        return True
    if center and right and not left:
        return True
    if left and not right and not center:
        return True
    if right and not left and not center:
        return True
    return False


def str_to_bool(s):
    """ ..^^. --> False, False, True, True, False"""
    return [c == '^' for c in s]


def bool_to_str(line_list):
    return ''.join(['.^'[c] for c in line_list])


def lcr(l):
    """ yield triplets: left, center, right. Pre- and append False """
    l = [False] + l + [False]
    for idx in range(1, len(l)-1):
        yield l[idx-1], l[idx], l[idx+1]


def next_line(line_list):
    return [is_trap(l, c, r) for l, c, r in lcr(line_list)]


def count_safe(l):
    """Count the number of False items in list"""
    return len(l) - sum(l)


def do(line_list, n):
    n_safe = count_safe(line_list)
    for _ in range(n-1):
        #print(bool_to_str(line_list))
        line_list = next_line(line_list)
        n_safe += count_safe(line_list)
    return n_safe


assert(do(str_to_bool('.^^.^.^^^^'), 10) == 38)

with open('input\input18.txt') as f:
    line = str_to_bool(f.readline().strip('\n'))

print('part A: ', do(line, 40))
print('part B: ', do(line, 400000))
