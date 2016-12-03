def check_triangle(x, y, z):
    return x + y > z and x + z > y and y + z > x


def find_number_of_possible_triangles(triangles):
    n = 0
    for column in zip(*triangles):
        for x, y, z in zip(column[::3], column[1::3], column[2::3]):
            if check_triangle(x, y, z):
                n += 1
    return n

with open('input/input3.txt') as f:
    triangles = [map(int, line.split()) for line in f.readlines()]
    print(find_number_of_possible_triangles(triangles))
