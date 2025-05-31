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
    A, B, C = map(int,input().split())
    GCD = gcd(A, B, C)

    ans = 0
    for e in [A, B, C]:
        ans += e // GCD - 1
    
    print(ans)



    

    

if __name__ == '__main__':
    main()