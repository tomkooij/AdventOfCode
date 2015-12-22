#adventofcode.com
#day6.1

INPUTFILE = 'input/input6'

SIZE = 1000

lights = SIZE*SIZE*[0]

def toggle(x): return (x+1) % 2
def on(x): return 1
def off(x): return 0

def do(f, x1, y1, x2, y2):

    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            lights[SIZE*x+y] = f(lights[SIZE*x+y])


with open(INPUTFILE) as f:
    lines = f.readlines()

    for line in lines:
        s = line.split(' ')
        if s[0] == 'toggle':
            x1,y1 = s[1].split(',')
            x2,y2 = s[3].split(',')
            do(toggle, int(x1),int(y1),int(x2),int(y2))
        if s[0] == 'turn' and s[1] == 'on':
            x1,y1 = s[2].split(',')
            x2,y2 = s[4].split(',')
            do(on, int(x1),int(y1),int(x2),int(y2))
        if s[0] == 'turn' and s[1] == 'off':
            x1,y1 = s[2].split(',')
            x2,y2 = s[4].split(',')
            do(off, int(x1),int(y1),int(x2),int(y2))

    print "brightness: ", sum(lights)
