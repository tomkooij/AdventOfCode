from day10 import knot_hash


def hex_to_binary(s):
    """convert hex string to binary string"""
    assert len(s) == 32
    return format(int(s, 16), '0>0128b')


def binary_to_maze(s):
    return s.replace('1', '#').replace('0', '.')


def create_maze(input):
    """return a 128x128 maze"""
    maze = []
    for i in range(128):
        s = input + '-' + str(i)
        h = knot_hash(list(s))
        b = hex_to_binary(h)
        assert len(b) == 128  # any leading zero's dropped?
        maze.append(binary_to_maze(b))
    return maze


def bfs_trace_group(maze, r, c):
    """
    Return all elements of group that contains (r, c)
    
    Just a BFS maze solver.
    
    based on maze solver from 2016 day 13
    """
    def is_valid(r, c):
        if r >= 0 and c >= 0 and r < 128 and c < 128:
            return maze[r][c] == '#'
        
    def generate_moves(pos):
        r, c = pos
        new_positions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        return [newpos for newpos in new_positions if is_valid(*newpos)]

    visited, queue = set(), [(r, c)]
    while queue:
        pos = queue.pop(0)
        if pos not in visited:
            visited.add(pos)
            queue.extend(generate_moves(pos))
    return visited
  

def solve(maze):
    """find all # and all groups"""
    visited = set()
    n_groups, n_wall = 0,0
    for r in range(128):
        for c in range(128):
            if maze[r][c] == '.':
                continue
            n_wall += 1
            if (r,c) in visited:
                continue
            group = bfs_trace_group(maze, r, c)
            visited.update(group)
            n_groups += 1
    return n_groups, n_wall 


input = 'stpzcrnm'

maze = create_maze(input)
n_groups, n_wall = solve(maze)
print('part a:', n_wall)
print('part b:', n_groups)
