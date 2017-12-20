def solve(maze):
    r, c = 0, maze[0].index('|')
    dr, dc = 1, 0
    
    tile = maze[r][c]
    assert tile ==  '|'
    
    letters = ''
    n_steps = 0

    while tile != ' ':
        if tile.isalpha():
            letters += tile
        if tile == '+':
            # switch from up/down to left/right or vv
            dr, dc = dc, dr
            if maze[r + dr][c + dc] == ' ':
                # wrong direction, flip:
                dr, dc = -dr, -dc
        r, c = r + dr, c + dc
        tile = maze[r][c]
        n_steps += 1

    return letters, n_steps


with open('input\input19.txt') as f:
    maze = f.readlines()
    a, b = solve(maze)
    print('part a: ', a)
    print('part b: ', b)