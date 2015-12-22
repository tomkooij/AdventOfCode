# adventofcode.com
# day 2.1

INPUTFILE = 'input/input2'

total = 0

with open(INPUTFILE) as f:
    lines = f.readlines()

    for line in lines:
        x, y, z = line.split('x')

        l = int(x)
        w = int(y)
        h = int(z)

        # the example is wrong! add the AREA of the smallest size
        area = 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)

        total += area

        #print l,w,h, area, total


print "Santa needs %d square feet of wrapping paper." % total
