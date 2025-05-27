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
    N, K = map(int,input().split())
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    operation = 0

    for i in range(N):
        operation += abs(A[i] - B[i])
        
    if operation <= K and (K - operation) % 2 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()