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
    A = list(map(int, input().split(' ')))
    ans = False
    
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] + A[j] + A[k] == 1000:
                    ans = True

    if ans:
        print('Yes')
    else:
        print('No')

    

if __name__ == '__main__':
    main()