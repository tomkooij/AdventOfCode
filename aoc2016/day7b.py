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


def is_aba(s):
    return s[0] != s[1] and s[0] == s[2]


def find_bab(aba, list):
    bab = aba[1]+aba[0]+aba[1]
    for item in list:
        if item.find(bab) != -1:
            return True
    return False


def test_hypernet_sequence(s):
    outside, inside = split_hypernet_sequence(s)
    for string in inside:
        for idx in range(len(string)-2):
            aba = string[idx:idx+3]
            if is_aba(aba):
                if find_bab(aba, outside):
                    return True
    for string in outside:
        for idx in range(len(string)-2):
            aba = string[idx:idx+3]
            if is_aba(aba):
                if find_bab(aba, inside):
                    return True
    return False


def testcases():
    print(test_hypernet_sequence('aba[bab]xyz'))
    print(test_hypernet_sequence('xyx[xyx]xyx'))
    print(test_hypernet_sequence('aaa[kek]eke'))
    print(test_hypernet_sequence('zazbz[bzb]cdb'))


with open('input/input7.txt') as f:
    testcases()
    supports_ssl = [test_hypernet_sequence(line) for line in f.readlines()]
    print(sum(supports_ssl))
