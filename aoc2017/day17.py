def stream(step, N=2018, full_list=True):
    """Return the full list or just first two items"""
    idx = 0
    l = [0]
    for length in range(1, N):
        # advance the list index and wrap
        idx += step + 1     
        idx %= length
        
        if full_list:
            l.insert(idx, length)
        elif idx == 0:
            l = [0, length]
    return l


input = 386

a = stream(input)
idx = a.index(2017)
print('part a:', a[idx:idx+2])
print('part b:', stream(input, N=50000000, full_list=False))