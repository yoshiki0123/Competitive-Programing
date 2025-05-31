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
    N, P, Q = map(int,input().split())
    A = list(map(int, input().split()))
    ans = 0
    for ptn in combinations(A, 5):
        tmp = 1
        for e in ptn:
            tmp *= e
            tmp %= P
        
        if tmp == Q:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()