# adventofcode.com
# day15

import numpy as np

INPUTFILE = 'input/input15'

TESTCASE = ['Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
            'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3']


def parse(lines):

    ingredients = np.array([4*[0] for _ in range(len(lines))])

    for idx, line in enumerate(lines):
        name, capcity, c, durability, d, flavor, f, texture, t, calories, cal = line.replace(',','').split()
        ingredients[idx] = map(int, (c,d,f,t))

    return ingredients

def score(n, ingredients):

    p = np.dot(n, ingredients)

    # negative values -> 0
    p = map(lambda x: max(0,x), p)

    # multiply all elements
    return reduce(lambda x,y: x*y, p)

if __name__ == '__main__':

    # Testcase
    ingredients = parse(TESTCASE)
    solution = []
    n = [0,0]
    for i in range(1,100):
        n[0] = i
        n[1] = 100 - n[0]
        solution.append((score(n, ingredients), n[0], n[1]))
    winner = max(solution)
    print winner
    assert winner[0] == 62842880, 'Testcase failure!'

    # part A
    with open(INPUTFILE, 'r') as f:
        lines = f.readlines()
    ingredients = parse(lines)
    solution = []
    n = [0, 0, 0, 0]
    for i in range(0,101):
        n[0] = i
        for j in range(0,101-i):
            n[1] = j
            for k in range(0,101-(i+j)):
                n[2] = k
                n[3] = 100 - (i+j+k)
                solution.append((score(n, ingredients), n[0], n[1], n[2], n[3]))
    winner = max(solution)
    print winner
