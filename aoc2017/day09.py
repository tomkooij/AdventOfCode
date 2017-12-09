from collections import deque


def remove_garbage(s, yield_garbage=False):
    queue = deque(s)
    garbage = False
    while queue:
        char = queue.popleft()
        #print('popped:', char)
        if char == '!':
            queue.popleft()
            continue
        if char == '>' and garbage:
            garbage = False
            continue
        if garbage:
            if yield_garbage:
                yield char
            continue
        if char == '<':
            garbage = True
            continue
        #print('yield: ', char)
        if not yield_garbage:
            yield char
              

def solve(s):
    score = 1
    total_score = 0
    for char in remove_garbage(s):
        if char == '{':
            total_score += score
            score += 1
        if char == '}':
            score -= 1
    return total_score


with open('input\input09.txt') as f:
    input = f.readline()
    print('part a:', solve(input))
    print('part b:', len(list(remove_garbage(input, yield_garbage=True))))