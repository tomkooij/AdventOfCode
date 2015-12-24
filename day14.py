# adventofcode.com
# day14

INPUTFILE = 'input/input14'
RUNTIME = 2503

TESTCASE = ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
            'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']


def parse(lines):

    reindeer = []
    for line in lines:
        name, can, fly, speed, km, f, flytime, seconds, but, t, m, r, f, resttime, sec = line.split()
        reindeer.append((name, int(speed), int(flytime), int(resttime)))
    return reindeer


def race(speed, flytime, resttime, racetime):

    time = flytime + resttime
    reps = racetime / time
    timeleft = racetime % time
    return (reps*flytime + min(timeleft, flytime))*speed


if __name__ == '__main__':

    #reindeer = parse(TESTCASE)
    with open(INPUTFILE, 'r') as f:
        lines = f.readlines()
    reindeer = parse(lines)

    solution = []
    for specs in reindeer:
        name, speed, flytime, resttime = specs
        distance = race(speed, flytime, resttime, RUNTIME)
        print name, distance
        solution.append((distance, name))

    print "winner: ", sorted(solution)[-1]
