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
    rotate based on position of letter X means that the whole string should be rotated to the right based on the index of letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
    """
    n  = l.index(a) + 1
    if n >= 5:
        n += 1
    l = deque(l)
    l.rotate(n)
    return list(l)

def reverse_pos(l, a, b):
    """
    reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
    """
    x = l.index(a)
    y = l.index(b)
    return l[:x] + list(reversed(l[x:y+1])) + l[y+1:]

def move_pos(l, x, y):
    """
    move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.
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
assert ''.join(reverse_pos(list('abcdefgh'), 'e', 'h')) == 'abcdhgfe'
assert ''.join(reverse_pos(list('abcdefgh'), 'a', 'c')) == 'cbadefgh'
assert ''.join(move_pos(list('abcdefgh'), 2, 0)) == 'cabdefgh'
