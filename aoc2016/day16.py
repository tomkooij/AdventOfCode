def reverse_order(s):
    """reverse a string"""
    return s[::-1]

replace = {'0': '1', '1': '0'}
def replace_0_1(s):
    """ '00110' --> '11001' """
    return ''.join([replace[c] for c in s])


def dragon_curve(a):
    return a + '0' + replace_0_1(reverse_order(a))


mapping = {'11': '1', '00': '1', '10': '0', '01': '0'}
def checksum(s):
    def checksum_step(s):
        return ''.join([mapping[s[idx:idx+2]] for idx in range(0, len(s), 2)])

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
print('part B: ', solve('11100010111110100', 35651584))
