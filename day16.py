# adventofcode.com
# day16

SPECS = 'input/specs16'
INPUT = 'input/input16'

def compare(spec, i):
    if partB:
        if spec == 'cats' or spec == 'trees':
            return specs[spec] < i
        elif spec == 'pomeranians' or spec == 'goldfish':
            return specs[spec] > i

    return specs[spec] == i

specs = {}
partB = True

with open(SPECS, 'r') as f:
    for line in f.readlines():
        d, i = line.split(': ')
        specs[d] = int(i)

with open(INPUT, 'r') as f:
    for line in f.readlines():
        _, number, spec1, i1, spec2, i2, spec3, i3 = line.replace(':','').replace(',','').split(' ')
        i1, i2, i3 = map(int, (i1, i2, i3))
        if compare(spec1, i1) and compare(spec2, i2) and compare(spec3, i3):
            print number, spec1, i2, spec2, i2, spec3, i3
