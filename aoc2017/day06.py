
def redistribute(lst):
    """naive implemention of the redistribute algorithm"""
    states = set()
    while True:
        n = max(lst)
        i = lst.index(n)
        lst[i] = 0
        while n:
            i += 1
            i %= len(lst)
            lst[i] += 1
            n -= 1
        if str(lst) in states:
            break
        states.add(str(lst))

    return len(states)+1


with open('input\input06.txt') as f:
    l = list(map(int, f.read().split()))
    print('part a:', redistribute(l))
    print('part b:', redistribute(l)-1)
    