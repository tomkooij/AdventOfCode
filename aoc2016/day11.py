"""
F4 .  .  .  .  .
F3 .  .  .  LG .
F2 .  HG .  .  .
F1 E  .  HM .  LM
"""
from itertools import combinations
from copy import deepcopy

# store state as list of gen-chip pairs.
initial_state = (0, [(1, 0), (2, 0)])  # (elevator, list of pairs)
goal = (3, [(3, 3), (3, 3)])

# input
initial_state = (0, [(0, 1), (0, 0), (0, 1), (0, 0), (0, 0)])
goal = (3, [(3, 3), (3, 3), (3, 3), (3, 3), (3, 3)])


def print_state(elevator, items):
    for floor in range(3, -1, -1):
        s = ['F'] + 3*(len(items)+1)*['.']
        s[1] = str(floor)
        if elevator == floor:
            s[3] = 'E'
        idx = 5
        for pair in items:
            if pair[0] == floor:
                s[idx] = 'G'
            if pair[1] == floor:
                s[idx+1] = 'M'
            idx += 3
        print(''.join(s))


def items_on_floor(floor, pairs):
    on_floor = []
    for idx, (gen, chip) in enumerate(pairs):
        if gen == floor:
            on_floor.append((idx, 0))  # (3,0) chip from pair 3 on floor
        if chip == floor:
            on_floor.append((idx, 1))
    return on_floor


def move(state, pair, item, move):
    new_state = deepcopy(state)
    p = state[pair]
    if item == 0:  # generator
        new_state[pair] = p[0]+move, p[1]
    if item == 1:
        new_state[pair] = p[0], p[1]+move
    return new_state

def generate_moves(moves, floor, pairs):
    items = items_on_floor(floor, pairs)
    new_pos = []
    for item1, item2 in combinations(items, 2):
        #print('moving comb up and down:', item1, item2)
        if floor < 3:
            after_item_1 = move(pairs, item1[0], item1[1], 1)
            new_pos.append((floor+1, move(after_item_1, item2[0], item2[1], 1)))
        if floor > 0:
            after_item_1 = move(pairs, item1[0], item1[1], -1)
            new_pos.append((floor-1, move(after_item_1, item2[0], item2[1], -1)))
    for item in items:
        #print('moving single up and down', item)
        if floor < 3:
            new_pos.append((floor+1, move(pairs, item[0], item[1], 1)))
        if floor > 0:
            new_pos.append((floor-1, move(pairs, item[0], item[1], -1)))

    #print('new_pos', new_pos)
    return [(moves+1, new_state) for new_state in new_pos]

def is_allowed(state):
    #print_state(*state)
    floor, pairs = state
    unpaired_microchip_on_floor = 4*[False]
    generator_on_floor = 4*[False]
    for pair in pairs:
        gen, mic = pair
        if gen != mic:
            unpaired_microchip_on_floor[mic] = True
    for pair in pairs:
        gen, mic = pair
        generator_on_floor[gen] = True

    #print('unpaired: ', unpaired_microchip_on_floor)
    #print('gen: ', generator_on_floor)
    for i in range(4):
        if unpaired_microchip_on_floor[i] and generator_on_floor[i]:
            return False
    return True


def bfs():
    depth = 0
    visited, queue = set(), [(0, initial_state)]
    while queue:
        #print ('queue', queue)
        moves, state = queue.pop(0)
        if moves > depth:
            print('reached depth = ', depth)
            depth = moves

        #print ('poped: ', moves, state)
        #print_state(*state)
        if not is_allowed(state):
            continue
        hash_state = str(state[0])+str(sorted(state[1]))
        if hash_state not in visited:
            visited.add(hash_state)
            if state == goal:
                return moves
            else:
                queue.extend(generate_moves(moves, *state))

print(bfs())
