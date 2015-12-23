# adventofcode
# day 9.1
# brute force exhaustive search of the travelling salesman problem (!?)

from collections import defaultdict
from itertools import permutations

INPUTFILE = 'input/input9'
TESTCASE = ['London to Dublin = 464','London to Belfast = 518','Dublin to Belfast = 141']

def distance(graph, route):
    """recusive computation of distance in graph via route"""

    nextstep = graph[route[0]][route[1]]  # distance between first and second city

    if len(route) > 2:
        return nextstep + distance(graph, route[1:])
    else:
        return nextstep

with open(INPUTFILE) as f:
    lines = f.readlines()

    graph = defaultdict(dict)  # graph of distances between cities (nodes)
    nodes = []

    for line in lines:
        _from, temp = line.split(' to ')
        _to, dist = temp.split(' = ')

        graph[_from][_to] = int(dist)
        graph[_to][_from] = int(dist)

        nodes.append(_from)
        nodes.append(_to)

nodes = list(set(nodes))

solution = []

for route in permutations(nodes):
    d = distance(graph, route)
    #print route, d
    solution.append(d)

print "min = ", min(solution)
print "max = ", max(solution)
