# adventofcode
# day11

INPUT = 'vzbxkghb'
#TESTCASE = 'abcdefgh'
TESTCASES = ['xyzaabb','aaaa', 'aacbb', 'acaabcaabb','acaabcaa', 'hijklmmn', 'abbceffg']

def next_char(c):
    """ a -> b, z -> a + carryflag """
    if c < 'z':
        return chr(ord(c)+1), 0
    elif c == 'z':
        return 'a', 1
    else:
        assert False, 'illegal input for next_char: %s' %c


def next_password(password):
    """ aab --> aac ,  aaz --> abz """

    nextpass = list(password)
    carry = 1
    idx = len(nextpass)-1
    while carry:
        nextpass[idx], carry = next_char(password[idx])
        idx -= 1
    return "".join(nextpass)


def is_valid(password):

    # illegal chars
    if 'i' in password: return False
    if 'o' in password: return False
    if 'l' in password: return False

    increasing = False
    for i in range(len(password)-2):
        if ord(password[i])==ord(password[i+1])-1 and ord(password[i])==ord(password[i+2])-2:
            increasing = True

    double = False
    for i in range(len(password)-1):
        if password[i]==password[i+1]:
            firstdouble = password[i]
            for i in range(i+2, len(password)-1):
                if password[i]==password[i+1] and password[i] != firstdouble:
                    double = True

    return increasing and double

for password in TESTCASES:
    print "%s is valid? %s" % (password, is_valid(password))

password = INPUT
print 'start: ', password
for _ in xrange(int(1e6)):
    password = next_password(password)
    if is_valid(password):
        print "Found valid next password: ", password
        break

for _ in xrange(int(1e7)):
    password = next_password(password)
    if is_valid(password):
        print "Found valid next password: ", password
        break
