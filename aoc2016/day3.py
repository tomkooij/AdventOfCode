def check_triangle(x, y, z):
    return x + y > z and x + z > y and y + z > x


with open('input/input3.txt') as f:
    n = 0
    for line in f.readlines():
        x, y, z = map(int, line.split())
        if check_triangle(x, y, z):
            n += 1
    print(n)
