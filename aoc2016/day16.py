def reverse_order(s):
    """reverse a string"""
    return s[::-1]


def replace_0_1(s):
    """ '00110' --> '11001' """
    result = []
    for char in s:
        if int(char):
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)


def dragon_curve(a):
    b = a
    return a + '0' + replace_0_1(reverse_order(b))


def checksum(s):
    def checksum_step(s):
        r = []
        mapping = {'11': '1',
                   '00': '1',
                   '10': '0',
                   '01': '0'}
        for idx in range(0, len(s), 2):
            r.append(mapping[s[idx:idx+2]])
        return ''.join(r)

    while True:
        s = checksum_step(s)
        if len(s) % 2:
            break
    return s


def solve(s, goal):
    while len(s) < goal:
        s = dragon_curve(s)
    return checksum(s[:goal])


def test():
    assert(reverse_order('100011') == '110001')
    assert(replace_0_1('00110') == '11001')
    assert(checksum('110010110100') == '100')

    testcases = [('0', '001'),
                 ('1', '100'),
                 ('11111', '11111000000'),
                 ('111100001010', '1111000010100101011110000')]

    for testcase, result in testcases:
        assert dragon_curve(testcase) == result
    assert(solve('10000', 20) == '01100')


test()
print('part A: ', solve('11100010111110100', 272))
print('part b: ', solve('11100010111110100', 35651584))
