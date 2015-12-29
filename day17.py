# adventofcode.com
# day17

from itertools import combinations

INPUT = 'input/input17'

with open(INPUT) as f:
    sizes = map(int, f.readlines())

total = 0
for size in range(len(sizes)-1):
    print "size: ", size
    for combi in combinations(sizes, size):
        if sum(combi) == 150:
            total += 1
    print "total: ", total
