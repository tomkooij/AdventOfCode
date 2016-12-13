
MAGIC = 1350
START = (1, 1)
GOAL = (39, 31)

WIDTH, HEIGHT = 100, 100

def is_wall_or_space(r, c):
    y, x = r, c
    if bin(x*x + 3*x + 2*x*y + y + y*y + MAGIC).count('1') % 2:
        return '#'
    else:
        return '.'

def print_maze(w, h):
    for r in range(h):
        print(''.join(maze[r][:w]))


def is_valid(r, c):
    return r >= 0 and c >= 0 and maze[r][c] == '.'


def generate_moves(moves, pos):
    r, c = pos
    new_positions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
    return [(moves+1, newpos) for newpos in new_positions if is_valid(*newpos)]


def bfs(start, goal, partB=False):
    visited, queue = set(), [(0, start)]
    while queue:
        moves, pos = queue.pop(0)
        if pos not in visited:
            visited.add(pos)
            if pos == goal:
                return moves
            if partB and moves == 50:
                return visited
            else:
                queue.extend(generate_moves(moves, pos))


maze = [[is_wall_or_space(r, c) for c in range(WIDTH)] for r in range(HEIGHT)]
print('part A', bfs(START, GOAL))
print('part B', len(bfs(START, GOAL, partB=True)))
