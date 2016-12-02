# adventofcode.com
# day 2.2

INPUTFILE = 'input/input2'

total = 0

with open(INPUTFILE) as f:
    lines = f.readlines()

    for line in lines:
        x, y, z = line.split('x')

        l = int(x)
        w = int(y)
        h = int(z)

        # wrap = 2 * smallest + 2 * nextsmallest
        ll = (l,w,h)
        wrap = 2*sorted(ll)[0] + 2*sorted(ll)[1]

        bow = l*w*h

        total += wrap+bow


print "Santa needs to order %d feet of ribbon." % total
