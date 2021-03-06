import hashlib
from collections import deque

SALT = 'ahsbgdzn'


def hex_str(i):
    return format(i, 'x')


def find_first_group(s, group):
    """ find group ('111') in string. Return letter ('1') of first match """
    r = []
    for item in group:
        if s.find(item) != -1:
            r.append((s.find(item), item))
    if len(r) > 0:
        return sorted(r)[0][1][0]


def find_quint(hashes, c):
    quint = 5*c
    for h in hashes:
        if quint in h:
            return True


def md5_hash(salt, i):
    item = salt+str(i)
    m = hashlib.md5()
    m.update(item.encode())
    return m.hexdigest()


def md5_hash_2016(salt, i):
    item = salt+str(i)
    for _ in range(2017):
        m = hashlib.md5()
        m.update(item.encode())
        item = m.hexdigest()
    return item


def find_otp(salt, md5_hash=md5_hash):
    """ search in a sliding window of 1000 hashes """

    queue = deque([md5_hash(salt, x) for x in range(1001)])
    triples = [3*hex_str(x) for x in range(16)]

    idx, n = 0, 0
    while queue:
        h = queue.popleft()
        c = find_first_group(h, triples)
        if c is not None:
            if find_quint(queue, c):
                n += 1
                print('found: ', n, idx)
                if n == 64:
                    return idx
        idx += 1
        queue.append(md5_hash(salt, idx+len(queue)))


print(find_otp(SALT))
print(find_otp(SALT, md5_hash=md5_hash_2016))
