from collections import deque


def swap_pos(l, x, y):
    l[x], l[y] = l[y], l[x]
    return l

def swap_letter(l, a, b):
    x = l.index(a)
    y = l.index(b)
    l[x], l[y] = l[y], l[x]
    return l

def rotate(l, n):
    """ n>0 rotate right"""
    l = deque(l)
    l.rotate(n)
    return list(l)

def rotate_pos(l, a):
    """
    rotate based on position of letter X means that the whole string should be
    rotated to the right based on the index of letter X (counting from 0) as
    determined before this instruction does any rotations. Once the index is
    determined, rotate the string to the right one time, plus a number of
    times equal to that index, plus one additional time if the index was at
    least 4.
    """
    n  = l.index(a) + 1
    if n >= 5:
        n += 1
    l = deque(l)
    l.rotate(n)
    return list(l)

def reversed_rotate_pos(l, a):
    mapping = {1: 1, 3: 2, 5: 3, 7: 4,
               0: 1, 2: 6, 4: 7, 6: 0}
    n = mapping[l.index(a)]
    l = deque(l)
    l.rotate(-n)
    return list(l)

def reverse_pos(l, x, y):
    """
    reverse positions X through Y means that the span of letters at indexes X
    through Y (including the letters at X and Y) should be reversed in order.
    """
    return l[:x] + list(reversed(l[x:y+1])) + l[y+1:]

def move_pos(l, x, y):
    """
    move position X to position Y means that the letter which is at index X
    should be removed from the string, then inserted such that it ends up at
    index Y.
    """
    letter = l.pop(x)
    l.insert(y, letter)
    return l


assert ''.join(swap_pos(list('abcdefgh'), 2, 3)) == 'abdcefgh'
assert ''.join(swap_letter(list('abcdefgh'), 'b', 'g')) == 'agcdefbh'
assert ''.join(rotate(list('abcdefgh'), 3)) == 'fghabcde'
assert ''.join(rotate(list('abcdefgh'), -2)) == 'cdefghab'
assert ''.join(rotate_pos(list('abcdefgh'), 'a')) == 'habcdefg'
assert ''.join(rotate_pos(list('abcdefgh'), 'e')) == 'cdefghab'
assert ''.join(reverse_pos(list('abcdefgh'), 4, 7)) == 'abcdhgfe'
assert ''.join(reverse_pos(list('abcdefgh'), 0, 2)) == 'cbadefgh'
assert ''.join(move_pos(list('abcdefgh'), 2, 0)) == 'cabdefgh'

# test reverse operations
l = list('abcdefgh')
for idx, letter in enumerate(l):
    tmp = rotate_pos(l, letter)
    reversed_tmp = reversed_rotate_pos(tmp, letter)
    #print(idx, letter, ''.join(tmp), tmp.index(letter), ''.join(reversed_tmp))
    assert reversed_tmp == l


def scramble(l, line):
    command, *rest = line.split()
    if command == 'swap':
        """
        swap position 7 with position 1
        swap letter e with letter d
        """
        if rest[0] == 'position':
            return swap_pos(l, int(rest[1]), int(rest[4]))
        if rest[0] == 'letter':
            return swap_letter(l, rest[1], rest[4])
    if command == 'move':
        """move position 4 to position 0"""
        assert rest[0] == 'position'
        return move_pos(l, int(rest[1]), int(rest[4]))
    if command == 'reverse':
        """reverse positions 3 through 7"""
        assert rest[0] == 'positions'
        return reverse_pos(l, int(rest[1]), int(rest[3]))
    if command == 'rotate':
        """rotate right 1 step"""
        if rest[0] == 'right':
            return rotate(l, int(rest[1]))
        elif rest[0] == 'left':
            return rotate(l, -int(rest[1]))
        elif rest[0] == 'based':
            """rotate based on position of letter a"""
            return rotate_pos(l, rest[5])
        else:
            print(line)
            assert False



def unscramble(l, line):
    """reverse operations """

    command, *rest = line.split()
    if command == 'swap':
        """
        swap position 7 with position 1
        swap letter e with letter d
        """
        if rest[0] == 'position':
            return swap_pos(l, int(rest[1]), int(rest[4]))
        if rest[0] == 'letter':
            return swap_letter(l, rest[1], rest[4])
    if command == 'move':
        """move position 4 to position 0"""
        assert rest[0] == 'position'
        return move_pos(l, int(rest[4]), int(rest[1]))
    if command == 'reverse':
        """reverse positions 3 through 7"""
        assert rest[0] == 'positions'
        return reverse_pos(l, int(rest[1]), int(rest[3]))
    if command == 'rotate':
        """rotate right 1 step"""
        if rest[0] == 'right':
            return rotate(l, -int(rest[1]))
        elif rest[0] == 'left':
            return rotate(l, int(rest[1]))
        elif rest[0] == 'based':
            """rotate based on position of letter a"""
            return reversed_rotate_pos(l, rest[5])

    print('lp0 on fire! ', line)
    assert False


with open('input\input21.txt') as f:
    lines = f.readlines()

l = list('abcdefgh')
for line in lines:
    l = scramble(l, line)

print('part A: ', ''.join(l))

l = list('fbgdceah')
for line in lines[::-1]:
    l = unscramble(l, line)
print('part B: ', ''.join(l))
