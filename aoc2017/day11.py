# Qbert directions, see docstring for cube_distance
# see also hexgrid.png

directions = {'n': (0,  1), 'ne': ( 1, 0), 'se': ( 1, -1),
              's': (0, -1), 'nw': (-1, 1), 'sw': (-1, 0)}


def cube_distance(x, y):
    """
    hexagonal cubes as in Q*bert game
    hexagons with flat tops
    
    x points 30degrees up (0,0)-(1,0)-(2,0)
    y points up (0,0)-(0,1)-(0,2)
    
    redundant axis z:
    z point 30degrees down (0,0)-(1,-1)-(2,-2)
    
    z = -(x+y)  sum(x,y,z)=0
    
    The shortest distance is always over a single axis:
    """
    z = -(x + y)
    return max(abs(x), abs(y), abs(z))


def do_moves(s):
    """yield all move in s"""
    for step in s.split(','):
        yield directions[step]

        
def solve(s):
    x, y = 0, 0
    max_d = 0
    for dx, dy in do_moves(s):
        x, y = x + dx, y + dy
        max_d = max(max_d, cube_distance(x,y))
    return cube_distance(x,y), max_d


with open('input\input11.txt') as f:
    input = f.read()
    d, max_d = solve(input)
    print('part a: ', d)
    print('part b: ', max_d)