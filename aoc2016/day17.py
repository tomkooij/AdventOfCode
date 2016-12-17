from collections import deque
import hashlib

MAGIC = 'udskfozm'


def md5_hash(s):
    m = hashlib.md5()
    m.update(s.encode())
    return m.hexdigest()


def can_move(path, r, c):
    hash_input = MAGIC+path[:-1]
    direction = path[-1]
    hash_ = md5_hash(hash_input)

    for idx, s in enumerate('UDLR'):
        if direction == s:
            return hash_[idx] in 'bcdef'


def is_valid(path, r, c):
    return r >= 0 and r < 4 and c >= 0 and c < 4 and can_move(path, r, c)


def generate_moves(path, pos):
    r, c = pos
    new_positions = [('D', (r+1, c)),
                     ('U', (r-1, c)),
                     ('R', (r, c+1)),
                     ('L', (r, c-1))]

    return [(path+move, newpos) for move, newpos in new_positions if
                                    is_valid(path+move, *newpos)]


def bfs(start, goal):
    paths = []
    queue = deque([('', start)])
    while queue:
        #print (queue)
        path, pos = queue.popleft()
        if pos == goal:
            paths.append(path)
        else:
            queue.extend(generate_moves(path, pos))
    return paths

solution = bfs((0, 0), (3, 3))
print('part A', solution[0])
print('part B', len(solution[-1]))
