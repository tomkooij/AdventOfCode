partB = False

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

    if partB:
        return len(s[:idx]) + n*decompress(nextpart) + decompress(rest)
    else:
        return len(s[:idx]) + n*len(nextpart) + decompress(rest)


with open('input/input9.txt') as f:
    s = f.readline().rstrip('\n')
    print('A: ', decompress(s))
    partB = True
    print('B: ', decompress(s))
