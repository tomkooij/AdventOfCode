# adventofcode.com
# day 4.1

import hashlib

SECRET = 'ckczppom'

for i in xrange(1,9999999):

    item = SECRET+str(i)

    m = hashlib.md5()
    m.update(item)
    if m.hexdigest()[0:5] == '00000':
        print "Found! ", item
        break
