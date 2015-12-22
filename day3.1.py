# adventofcode.com
# day 3.1

INPUTFILE = 'input/input3'

TESTCASE1 = '>'
TESTCASE2 = '^>v<'
TESTCASE3 = '^v^v^v^v^v'

total = 0

UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'

x,y = 0,0
trip = []  # list of locations

with open(INPUTFILE) as f:
    inputstr = f.readline()
    #inputstr = TESTCASE2

    # start position
    trip.append((x,y))

    for char in inputstr:

        if char == UP:
            y += 1
        elif char == DOWN:
            y -= 1
        elif char == LEFT:
            x -= 1
        elif char == RIGHT:
            x += 1
        else:
            print "skipping unkown input: ", char

        trip.append((x,y))

    # remove duplicates
    trip = set(trip)

    print "Santa visited %d unique locations" % len(trip)
