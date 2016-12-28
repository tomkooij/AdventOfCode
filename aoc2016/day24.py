from collections import defaultdict
from itertools import permutations

def find_digits(maze):
    digits = {}
    for r, row in enumerate(maze):
        for c, char in enumerate(row):
            if char.isdigit():
                digits[int(char)] = (r,c)
    return digits


def is_valid(r, c):
    return maze[r][c] != '#'


def generate_moves(moves, pos):
    r, c = pos
    new_positions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
    return [(moves+1, newpos) for newpos in new_positions if is_valid(*newpos)]


def bfs(start, goal):
    visited, queue = set(), [(0, start)]
    while queue:
        moves, pos = queue.pop(0)
        if pos not in visited:
            visited.add(pos)
            if pos == goal:
                return moves
            else:
                queue.extend(generate_moves(moves, pos))



with open('input\input24.txt') as f:
    maze = [line.strip('\n') for line in f.readlines()]

locations = find_digits(maze)

n = len(locations.keys())
dist = defaultdict(dict)
for j in range(n):
    for i in range(j, n):
        dist[i][j] = bfs(locations[i], locations[j])
        dist[j][i] = dist[i][j]

min_d_A, min_d_B = 10000, 10000
for p in permutations(range(n)):
    d, start = 0, 0
    for end in p:
        d += dist[start][end]
        start = end
    min_d_A = min(min_d_A, d)
    min_d_B = min(min_d_B, d+dist[start][0])
print('part A: ', min_d_A)
print('part B: ', min_d_B)
