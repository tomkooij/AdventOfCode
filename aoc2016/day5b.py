import hashlib

SECRET = 'ojvtpuvg'


def find_next(secret, startidx):
    for i in range(startidx, 99999999):
        item = secret+str(i)
        m = hashlib.md5()
        m.update(item.encode())
        if m.hexdigest()[0:5] == '00000':
            return i, m.hexdigest()[5], m.hexdigest()[6]

n = 0
id = 16*['_']

while True:
    n, pos, char = find_next(SECRET, n+1)
    pos = int(pos, 16)

    if id[pos] != '_':
        continue

    id[pos] = char
    print('found: ', n, char, pos, ''.join(id))

    if '_' not in id[:8]:
        break

print(''.join(id[:8]))
