def parse(string):
    name, checksum = string.split('[')
    checksum = checksum[:-1]  # remove ] bracket
    name, code = name.rsplit('-', 1)
    return name, int(code), checksum


def shift_char(c, n):
    if c == '-':
        return '-'
    char = ord(c) + n
    if char > ord('z'):
        char -= 26
    return chr(char)


def decrypt(string):
    name, code, checksum = parse(string)
    shift = code % 26
    decrypted_name = ''.join([shift_char(char, shift) for char in name])
    return code, decrypted_name


with open('input/input4.txt') as f:
    names = [decrypt(line.rstrip('\n')) for line in f.readlines()]
    for code, name in names:
        if 'north' in name:
            print(code, name)
