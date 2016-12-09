partB = False

def decompress(s):

    if '(' not in s:
        return len(s)

    start, marker = s.split('(', 1)
    marker, rest = marker.split(')', 1)
    number_of_chars, n = map(int, marker.split('x'))

    nextpart = rest[:number_of_chars]
    rest = rest[number_of_chars:]

    if partB:
        return len(start) + n*decompress(nextpart) + decompress(rest)
    else:
        return len(start) + n*len(nextpart) + decompress(rest)


with open('input/input9.txt') as f:
    s = f.readline().rstrip('\n')
    print('A: ', decompress(s))
    partB = True
    print('B: ', decompress(s))
