# adventofcode.com
# day14.2

INPUTFILE = 'input/input14'
RUNTIME = 2503

TESTCASE = ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
            'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']
#RUNTIME = 1000

def parse(lines):
    reindeer = []
    for line in lines:
        beast = {}
        name, can, fly, speed, km, f, flytime, seconds, but, t, m, r, f, resttime, sec = line.split()
        beast['name'] = name
        beast['speed'] = int(speed)
        beast['flytime'] = int(flytime)
        beast['resttime']=  int(resttime)
        beast['distance'] = 0
        beast['score'] = 0
        reindeer.append(beast)
    return reindeer


def is_resting(time, beast):

    flytime = beast['flytime']
    resttime = beast['resttime']

    timeleft = time % (flytime+resttime)
    if flytime <= timeleft:
        return True
    return False


if __name__ == '__main__':

    with open(INPUTFILE, 'r') as f:
        lines = f.readlines()
    reindeer = parse(lines)

    #reindeer = parse(TESTCASE)

    for time in range(0,RUNTIME+1):
        for beast in reindeer:
            if not is_resting(time, beast):
                beast['distance'] += beast['speed']

        # every reindeer in the lead gets 1 point
        high = 0
        for beast in sorted(reindeer, key=lambda k: k['distance'], reverse=True):
            if beast['distance'] < high:
                break
            beast['score'] += 1
            high = beast['distance']

    winner = sorted(reindeer, key=lambda k: k['score'], reverse=True)[0]
    print "After %d seconds %s wins with %d points!" % (RUNTIME, winner['name'], winner['score'])
