# coding: utf-8
from collections import deque
from functools import reduce


def reverse(l, start, inc):
    """
    replace part of list with its reverse
    from index start to start+inc
    
    stupid lazy (as in programmer being lazy) implementation  
    """
    d = deque(l)
    d.rotate(-start)  # prevent wrapping, rotate start to index 0
    
    l = list(d)
    x = l[:]
    x = x[:inc]   # select
    x.reverse()   # reverse
    l[:inc] = x  # replace
    
    d = deque(l)
    d.rotate(start)
    return list(d)
 

def knot_hash(input, rounds=1, n=256):  
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


def solve_part_b(input):
    l = [ord(x) for x in input]
    l += [17, 31, 73, 47, 23]
    x = knot_hash(l, rounds=64)
    return create_hash(x)


with open('input\input10.txt') as f:
    input_str = f.read()
    input_list = map(int, input_str.split(','))
    x = knot_hash(input_list)
    print('part a: ', x[0]*x[1])
    print('part b: ', solve_part_b(input_str))
