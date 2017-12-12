def parse(row):
    n, rest = row.split('<->')
    return int(n), list(map(int, rest.split(',')))


def find_group(links, start=0):  
    """BFS for all elements of group"""
    queue = set([start])
    group = set()
    while queue:
        n = queue.pop()
        group.add(n)
        for i in links[n]:
            if i in group:
                continue
            queue.add(i)
    return group


def group_lengths(links):
    """return the lengths of all groups"""
    lengths = []
    while links:
        start_item = list(links.keys())[0] 
        g = find_group(links, start_item)
        lengths.append(len(g))
        # remove group from links
        for key in g:
            links.pop(key)
    return lengths


with open('input\input12.txt') as f:
    rows = [parse(row) for row in f.readlines()]
    links = {}
    for n, l in rows:
        links[n] = l
    lengths = group_lengths(links)
    print('part a: ', lengths[0])
    print('part b: ', len(lengths))
