def position(r, t):
    """calculate the position of a layer with range r at time t"""
    return t % (2 * (r - 1))


def score(fw):
    score = 0
    for x, r in fw.items():
        if position(r, x) == 0:
            score += x * r
    return score


def brute_force(fw):
    """Brute force. prevent function calls for speed"""
    
    delay = 0
    while True:
        for x, r in fw.items():
            t = x + delay
            if t % (2 * (r - 1)) == 0:
                delay += 1
                break  
        else:
            return delay 
        
    
with open('input\input13.txt') as f:
    rows = f.readlines()
    firewall = {}
    for item in rows:
        x,n = map(int, item.split(':'))
        firewall[x] = n

    print('part a:', score(firewall))  
    print('part b:', brute_force(firewall))