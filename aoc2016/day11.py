
initial_states = [('part A', [8, 2, 0, 0]),
                  ('part B', [12, 2, 0, 0])]

for case, state in initial_states:
    print(case, state)
    moves = 0
    for floor in range(3):
        n_items = state[floor]
        moves += 2 * n_items - 3
        state[floor+1] += state[floor]
        state[floor] = 0
        print(floor, moves, state)
