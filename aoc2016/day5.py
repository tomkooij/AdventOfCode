import hashlib

SECRET = 'ojvtpuvg'


def find_next(secret, startidx):
    for i in range(startidx, 999999999):

        item = secret+str(i)

        m = hashlib.md5()
        m.update(item.encode())
        if m.hexdigest()[0:5] == '00000':
            return i, m.hexdigest()[5]

n = 0
id = ''

for _ in range(8):
    n, char = find_next(SECRET, n+1)
    id += char
    print('found: ', n, char, id)

print(id)
