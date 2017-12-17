from collections import deque
        

def solve(start_position='abcdefghijklmnop', N=1):
    q = deque(start_position)
    stack = [start_position]

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
            return stack[N % i] 
            
        stack.append(''.join(q))
    
    return new_position


with open('input\input16.txt') as f:
    instructions = f.read().split(',')
    print('part a:',solve(N=1))
    print('part b:',solve(N=int(1e9)))