#!/bin/python

import sys

def make_change(coins, n):
    ways = [0] * (n + 1)
    ways[0] = 1

    for c in coins:
        for x in range(c, n + 1):
            ways[x] += ways[x - c]

    return ways[n]
    
n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
coins = map(int,raw_input().strip().split(' '))
print make_change(coins, n)