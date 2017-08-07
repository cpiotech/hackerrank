#!/bin/python

import sys
import heapq

min_h = []
max_h = []

n = int(raw_input().strip())
a = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())

    if not max_h or a_t < abs(max_h[0]):
        heapq.heappush(max_h, -a_t)
    else:
        heapq.heappush(min_h, a_t)

    if len(min_h) - len(max_h) > 1:
        heapq.heappush(max_h, -heapq.heappop(min_h))
    elif len(max_h) - len(min_h) > 1:
        heapq.heappush(min_h, -heapq.heappop(max_h))

    if len(min_h) == len(max_h):
        print float(min_h[0] - max_h[0]) / 2.0
    elif len(min_h) < len(max_h):
        print float(-max_h[0])
    else:
        print float(min_h[0])
