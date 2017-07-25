#!/bin/python

import sys

def lonely_integer(a):
    res = 0
    for n in a:
        res ^= n
    return res

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)