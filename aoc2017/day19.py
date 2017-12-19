def solve(maze):
    r, c = 0, maze[0].index('|')
    dr, dc = 1, 0

    letters = ''
    n_steps = 0

    while True:
        n_steps += 1
        r, c = r + dr, c + dc
        tile = maze[r][c]
        if tile == ' ':
            break 
        if tile.isalpha():
            letters += tile
        if tile != '+':
            continue
        # switch from up/down to left/right or vv
        dr = 1 - abs(dr)
        dc = 1 - abs(dc)
        if maze[r + dr][c + dc] == ' ':
            # wrong direction, flip:
            dr, dc = -dr, -dc
    return letters, n_steps


with open('input\input19.txt') as f:
    maze = f.readlines()
    a, b = solve(maze)
    print('part a: ', a)
    print('part b: ', b)