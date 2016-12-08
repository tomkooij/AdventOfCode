def split_string_brackets(s):
    """ abc[xyz]ghf --> abc, xyz, ghf """
    try:
        first, next_part = s.split('[', 1)
        second, third = next_part.split(']', 1)
        return first, second, third
    except ValueError:
        return s, '', None


def split_hypernet_sequence(s):
    A, B = [], []
    while s is not None:
        first, second, third = split_string_brackets(s)
        A.append(first)
        B.append(second)
        s = third
    return A, B


def abba(s):
    return s[0] != s[1] and s[0] == s[3] and s[1] == s[2]


def test_hypernet_sequence(s):
    outside, inside = split_hypernet_sequence(s)
    for string in inside:
        for idx in range(len(string)-3):
            if abba(string[idx:idx+4]):
                return False
    for string in outside:
        for idx in range(len(string)-3):
            if abba(string[idx:idx+4]):
                return True
    return False


def testcases():
    print(test_hypernet_sequence('abba[mnop]qrst'))
    print(test_hypernet_sequence('abcd[bddb]xyyx'))
    print(test_hypernet_sequence('aaaa[qwer]tyui'))
    print(test_hypernet_sequence('ioxxoj[asdfgh]zxcvbn'))


with open('input/input7.txt') as f:
    testcases()
    valid_tls = [test_hypernet_sequence(line) for line in f.readlines()]
    print(sum(valid_tls))
