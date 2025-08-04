#library
import sys, re, heapq
from math import sin, cos, radians, ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

#class

#def

#main
def main():
    N = int(input())
    xy = []
    for _ in range(N):
        x, y = map(int,input().split())
        xy.append((x, y))
    
    ans = 0
    for p1 in xy:
        for p2 in xy:
            length = sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
            ans = max(ans, length)
    
    print(ans)
    

if __name__ == '__main__':
    main()