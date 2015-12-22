#adventofcode.com
#day6.1

INPUTFILE = 'input/input6'

SIZE = 1000

lights = SIZE*SIZE*[0]

def toggle(x1,y1,x2,y2):
    #print "toggle: ", x1, y1, x2, y2
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            lights[SIZE*x+y] += 2

def on(x1,y1,x2,y2):
    #print "on: ", x1, y1, x2, y2
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            lights[SIZE*x+y] += 1

def off(x1,y1,x2,y2):
    #print "off: ", x1, y1, x2, y2
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            lights[SIZE*x+y] -= 1
            if lights[SIZE*x+y] < 0:
                lights[SIZE*x+y] = 0


with open(INPUTFILE) as f:
    lines = f.readlines()

    for line in lines:
        s = line.split(' ')
        if s[0] == 'toggle':
            x1,y1 = s[1].split(',')
            x2,y2 = s[3].split(',')
            toggle(int(x1),int(y1),int(x2),int(y2))
        if s[0] == 'turn' and s[1] == 'on':
            x1,y1 = s[2].split(',')
            x2,y2 = s[4].split(',')
            on(int(x1),int(y1),int(x2),int(y2))
        if s[0] == 'turn' and s[1] == 'off':
            x1,y1 = s[2].split(',')
            x2,y2 = s[4].split(',')
            off(int(x1),int(y1),int(x2),int(y2))

    print "brightness: ", sum(lights)
