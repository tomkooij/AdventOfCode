# adventofcode.com
# day 4.2

import hashlib

SECRET = 'ckczppom'

for i in xrange(1,9999999):

    if not i % 100000:
        print i

    item = SECRET+str(i)

    m = hashlib.md5()
    m.update(item)
    if m.hexdigest()[0:6] == '000000':
        print "Found! ", item
        break
