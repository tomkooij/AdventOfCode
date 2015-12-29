# adventofcode
# day20

TEST = 33100000
HIGH = int(1e7)

if __name__ == '__main__':

    print "part B"
    house = (HIGH) * [0]

    for i in xrange(1, HIGH):
        for j in xrange(i, min(i*51, HIGH/10), i):
            house[j] += i * 11

    print "max = ", max(house)

    for idx in xrange(HIGH):
        if house[idx] > TEST:
            print "found %d at index %d: %d" % (TEST, idx, house[idx])
            break
