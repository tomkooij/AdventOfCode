from collections import deque
from hashlib import md5

MAGIC = 'udskfozm'


def md5_hash(s):
    return md5(s.encode()).hexdigest()


move_to_index = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
def can_move(path, move):
    return md5_hash(MAGIC+path)[move_to_index[move]] in 'bcdef'


def is_valid(r, c):
    return r >= 0 and r < 4 and c >= 0 and c < 4


def generate_moves(path, r, c):
    new_positions = [('D', (r+1, c)),
                     ('U', (r-1, c)),
                     ('R', (r, c+1)),
                     ('L', (r, c-1))]

    return [(path+move, newpos) for move, newpos in new_positions if
                            is_valid(*newpos) and can_move(path, move)]


def bfs(start, goal):
    paths = []
    queue = deque([('', start)])
    while queue:
        #print (queue)
        path, pos = queue.popleft()
        if pos == goal:
            paths.append(path)
        else:
            queue.extend(generate_moves(path, *pos))
    return paths

solution = bfs((0, 0), (3, 3))
print('part A', solution[0])
print('part B', len(solution[-1]))
