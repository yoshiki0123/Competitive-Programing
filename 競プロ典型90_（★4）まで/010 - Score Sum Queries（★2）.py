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
    CP_sums = [(0, 0)]
    sum_1 = 0
    sum_2 = 0
    for _ in range(N):
        C, P = map(int,input().split())
        if C == 1:
            sum_1 += P
        else:
            sum_2 += P
        CP_sums.append((sum_1, sum_2))

    Q = int(input())
    for _ in range(Q):
        L, R = map(int,input().split())
        print(CP_sums[R][0] - CP_sums[L-1][0], CP_sums[R][1] - CP_sums[L-1][1])

        
    
        
        
    

if __name__ == '__main__':
    main()