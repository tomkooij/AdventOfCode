# adventofcode.com
# day16

SPECS = 'input/specs16'
INPUT = 'input/input16'

specs = {}

with open(SPECS, 'r') as f:
    for line in f.readlines():
        d, i = line.split(': ')
        specs[d] = int(i)

with open(INPUT, 'r') as f:
    for line in f.readlines():
        _, number, spec1, i1, spec2, i2, spec3, i3 = line.replace(':','').replace(',','').split(' ')
        if specs[spec1] == int(i1) and specs[spec2] == int(i2) and specs[spec3] == int(i3):
            print number, spec1, i2, spec2, i2, spec3, i3
