testcases = [('(3x3)XYZ', 9),
             ('X(8x2)(3x3)ABCY', 20),
             ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
             ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445)]


def decompress(s):

    idx = s.find('(')
    if idx == -1:
        return len(s)

    idx_endmarker = s.find(')', idx)
    marker = s[idx+1:idx_endmarker]
    number_of_chars, n = map(int, marker.split('x'))

    start = idx_endmarker+1
    endpart = idx_endmarker+number_of_chars+1
    nextpart = s[start: endpart]
    rest = s[endpart:]

    return len(s[:idx]) + n*decompress(nextpart) + decompress(rest)


for testcase, result in testcases:
    print (testcase)
    length = decompress(testcase)
    print (length, result)
    assert length == result


with open('input/input9.txt') as f:
    print(decompress(f.readline().rstrip('\n')))
