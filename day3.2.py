# adventofcode.com
# day 3.1

INPUTFILE = 'input/input3'

TESTCASE1 = '^v'
TESTCASE2 = '^>v<'
TESTCASE3 = '^v^v^v^v^v'

UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'

x, y = 0, 0  # santa location
rx, ry = 0, 0  # robosanta location

trip = []  # list of locations


def move(char, x, y):
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

    return x, y


with open(INPUTFILE) as f:
    inputstr = f.readline()
    #inputstr = TESTCASE3

    # start position
    trip.append((x, y))

    for idx, char in enumerate(inputstr, start=1):
        if idx % 2:
            # santa moves
            x, y = move(char, x, y)
            trip.append((x, y))
        else:
            # robo santa moves this turn
            rx, ry = move(char, rx, ry)
            trip.append((rx, ry))

    #print trip
    # remove duplicates
    trip = set(trip)

    print "Santa visited %d unique locations" % len(trip)
