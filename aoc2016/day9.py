testcases = [('ADVENT', 'ADVENT'),
            ('A(1x5)BC', 'ABBBBBC'),
            ('(3x3)XYZ', 'XYZXYZXYZ'),
            ('A(2x2)BCD(2x2)EFG', 'ABCBCDEFEFG'),
            ('(6x1)(1x3)A', '(1x3)A'),
            ('X(8x2)(3x3)ABCY', 'X(3x3)ABC(3x3)ABCY')]


def decompress(s):

    idx = s.find('(')
    if idx == -1:
        return s

    idx_endmarker = s.find(')', idx)
    marker = s[idx+1:idx_endmarker]
    number_of_chars, n = map(int, marker.split('x'))

    start = idx_endmarker+1
    end = idx_endmarker+number_of_chars+1
    repeat = s[start: end]
    rest = s[end:]

    return s[:idx] + n*repeat + decompress(rest)


for testcase, result in testcases:
    print (testcase)
    length = decompress(testcase)
    print (length, result)
    assert length == result


with open('input/input9.txt') as f:
    print(len(decompress(f.readline().rstrip('\n'))))
