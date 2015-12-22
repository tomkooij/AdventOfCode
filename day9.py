# adventofcode
# day 9.1
# brute force exhaustive search of the travelling salesman problem (!?)

from collections import defaultdict
from itertools import permutations

INPUTFILE = 'input/input9'
TESTCASE = ['London to Dublin = 464','London to Belfast = 518','Dublin to Belfast = 141']

def distance(graph, route):
    nextstep = graph[route[0]][route[1]]

    if len(route) > 2:
        return nextstep + distance(graph, route[1:])
    else:
        return nextstep

with open(INPUTFILE) as f:
    lines = f.readlines()

    graph = defaultdict(dict)
    nodes = []

    for line in lines:
        s = line.split()
        assert (s[1] == 'to') and (s[3] == '=')

        graph[s[0]][s[2]] = int(s[4])
        graph[s[2]][s[0]] = int(s[4])

        nodes.append(s[0])
        nodes.append(s[2])

routes = list(set(nodes))

solution = []

for route in permutations(routes):
    d = distance(graph, route)
    #print route, d
    solution.append(d)
print "min = ", min(solution)
print "max = ", max(solution)

#print graph
