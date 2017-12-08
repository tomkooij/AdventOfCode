from collections import defaultdict


def create_tree(rows):
    weights = defaultdict(int)
    leafs = defaultdict(list)
    for row in rows:
        base, weight, *rest = row
        weights[base] = int(weight[1:-1])
        if len(rest):
            assert rest[0] == '->'
            for item in rest[1:]:
                leafs[base].append(item.strip(','))
    return weights, leafs


def calc_weight(part):
    
    if not len(leafs[part]):
        return weights[part]
    
    return weights[part] + sum([calc_weight(i) for i in leafs[part]])


def find_imbalance(weights, leafs, base):
    """walk the tree from trunk to leafs"""
    while True:
        #print('searching: ', base)
        w = [calc_weight(leaf) for leaf in leafs[base]]
        if len(set(w)) == 1:
            #print('found!', base, delta)
            break
        i = w.index(max(w))
        delta = max(w) - min(w)
        base = leafs[base][i]
        
    return weights[base]-delta


with open('input\input07.txt') as f:
    rows = [row.strip().split() for row in f.readlines()]
    weights, leafs = create_tree(rows)
    leafs_set = set()
    for key in leafs:
        leafs_set.update(leafs[key])
    difference = set(weights) - leafs_set
    trunk = difference.pop()
    print('part a', trunk)
    print('part b', find_imbalance(weights, leafs, trunk))
    
        
    