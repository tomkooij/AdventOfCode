# adventofcode.com
# day 4.1

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
id = 10*['_']
done = set()

while True:
    n, pos, char = find_next(SECRET, n+1)
    try:
        pos = int(pos)
    except:
        continue
    if pos in done:
        continue
    done.add(pos)

    id[pos] = char
    print('found: ', n, char, pos, id)
    if len(done) >= 10:
        break

print(''.join(id[:8]))
