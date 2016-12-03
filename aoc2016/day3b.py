import re
import numpy as np


def check_triangle(x, y, z):
    return x + y > z and x + z > y and y + z > x


def find_number_of_possible_triangles(triangles):
    n = 0
    triangles = np.array(triangles)
    for t in triangles.T:  # for each column
        for x, y, z in zip(t[::3], t[1::3], t[2::3]):
            if check_triangle(x, y, z):
                n += 1
    return n

with open('input/input3.txt') as f:
    triangles = []
    for line in f.readlines():
        x, y, z = map(int, re.findall(r'\d+', line))
        triangles.append((x, y, z))
    print(find_number_of_possible_triangles(triangles))
