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
    A = sorted(A)
    B = list(map(int, input().split(' ')))
    B = sorted(B)

    ans = 0
    for i in range(N):
        ans += abs(A[i]-B[i])
    
    print(ans)

    
    

if __name__ == '__main__':
    main()