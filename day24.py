# adventofcode
# day 24

from itertools import combinations

INPUTFILE = 'input/input24'
TESTCASE = range(1,6) + range(7,12)

NUMBER_OF_BINS = 4

def find_parts(weights, target, length):
    found = []
    for i in range(1,length):
        for firstpart in combinations(weights, i):
            if sum(firstpart) != target: continue
            found.append(firstpart)
    return set(found)

if __name__ == '__main__':
    with open(INPUTFILE, 'r') as f:
        lines = f.readlines()
    weights = set([int(x) for x in lines])
    #weights = set(TESTCASE)

    bintotal = sum(weights)/NUMBER_OF_BINS
    print "Dataset has %d weights. %d Bins. Binsize = %d" % (len(weights), NUMBER_OF_BINS, bintotal)

    firstparts = find_parts(weights, bintotal, len(weights)/3)
    print 'number of unique firstparts:', len(firstparts)

    shortestpart = min([len(x) for x in firstparts])

    firstparts = [x for x in firstparts if len(x) == shortestpart]
    print 'length of shortest firstparts: ', len(firstparts[0])
    fast_min_QE = min(reduce(lambda x,y: x*y, p) for p in firstparts)
    print 'predicted min QE: ', fast_min_QE
    #print 'firstparts: ', firstparts


    assert NUMBER_OF_BINS == 3, 'Full search only implemented for 3 bins'
    # full search of parts 2 and 3 foreach part 1
    QE = []
    for i, part1 in enumerate(firstparts, start=1):
        if not i % 1000: print '%d firstparts searched.' % i
        rest = weights - set(part1)
        restparts = find_parts(rest, bintotal, len(weights)/2)
        for part2 in restparts:
            part3 = rest - set(part2)
            if sum(part3) == bintotal:
                #print "found: ", part1, part2, part3
                QE.append(reduce(lambda x,y: x*y, part1))

    print "min QE after fullsearch = ", min(QE)
