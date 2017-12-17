from collections import deque
        

def solve(instructions, start_position='abcdefghijklmnop', N=1):
    q = deque(start_position)
    cache = [start_position]

    for i in range(1, N+1):  

        for instruction in instructions:
            ins = instruction[0]
            if ins == 'p':
                a, b = instruction[1:].split('/')
                x = q.index(a)
                y = q.index(b)
                q[x], q[y] = q[y], q[x] 
            if ins == 'x':
                a, b = map(int, instruction[1:].split('/'))
                q[a], q[b] = q[b], q[a] 
            if ins == 's':
                x = int(instruction[1:])
                q.rotate(x)      
        new_position = ''.join(q)
        
        if new_position == start_position:
            #found a duplicate --> sequence will repeat.
            #period of the sequence is `i` since we count from
            #start position.  
            return cache[N % i] 
            
        cache.append(new_position)
    
    return new_position


with open('input\input16.txt') as f:
    instructions = f.read().split(',')
    print('part a:', solve(instructions, N=1))
    print('part b:', solve(instructions, N=int(1e9)))