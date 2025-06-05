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
    A =  list(map(int, input().split(' '))) 
    A = sorted(A)
    Q = int(input())

    for _ in range(Q):
        B = int(input())
        if B < A[0]:
            print(A[0]-B)
            continue
        if A[-1] <= B:
            print(B-A[-1])
            continue
        ok = 0
        ng = len(A) - 1
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if A[mid] <= B:
                ok = mid
            else:
                ng = mid
        print(min(abs(B-A[ok]), abs(A[ng]-B)))


if __name__ == '__main__':
    main()