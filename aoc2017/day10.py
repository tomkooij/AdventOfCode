# coding: utf-8
from collections import deque
from functools import reduce


def reverse(l, start, inc):
    """
    replace part of list with its reverse
    from index start to start+inc
    
    stupid lazy (as in programmer being lazy) implementation:
     First rotate the element with index start to index 0
     Select, reverse, replace
     Rotate the list back to its previous state
    """
    d = deque(l)
    d.rotate(-start)

    l = list(d)
    x = l[:inc]   # select
    x.reverse()   # reverse
    l[:inc] = x  # replace

    d = deque(l)
    d.rotate(start)

    return list(d)
 

def knot_hash_rounds(input, rounds=1, n=256):  
    skip = 0
    index = 0
    x = list(range(n))
    for _ in range(rounds):
        for length in input:
            x = reverse(x, index, length)
            index += length + skip
            index %= n
            skip +=1
            #print(index, skip, x)
    return x
        

def xor_list(l):
    return reduce(lambda x, y: x ^ y, l)


def create_hash(x):
    """xor each part of 16 numbers and convert to hex string"""
    return ''.join(["{0:x}".format(xor_list(x[i:i+16])) 
                   for i in list(range(0, len(x), 16))])


def knot_hash(s):
    l = [ord(x) for x in s]
    l += [17, 31, 73, 47, 23]
    x = knot_hash_rounds(l, rounds=64)
    return create_hash(x)


if __name__ == '__main__':
    with open('input\input10.txt') as f:
        input_str = f.read()
        input_list = map(int, input_str.split(','))
        x = knot_hash_rounds(input_list)
        print('part a: ', x[0]*x[1])
        print('part b: ', knot_hash(input_str))
