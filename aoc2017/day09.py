from collections import deque


def remove_garbage(s, count_garbage=False):
    queue = deque(s)
    garbage = False
    chars_in_garbage = 0
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
            chars_in_garbage += 1
            continue
        if char == '<':
            garbage = True
            continue
        #print('yield: ', char)
        if not count_garbage:
            yield char
    if count_garbage:
        yield chars_in_garbage
           

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
    print('part b:', next(remove_garbage(input, count_garbage=True)))