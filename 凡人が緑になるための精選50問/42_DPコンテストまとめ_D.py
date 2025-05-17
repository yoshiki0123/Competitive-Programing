#library
import sys, re, heapq
from math import sin, cos, radians, ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

#class

#def


#main
def main():
    N, W = map(int,input().split())
    items = [(0, 0)]
    for _ in range(N):
        w, v = map(int,input().split())
        items.append((w, v))
    dp = [[0]*(W+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        w, v = items[i]
        for j in range(W+1):
            if 0 <= i-1 <= N-1 and 0 <= j-w <= W:
                dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    
    print(dp[N][W])
    
if __name__ == '__main__':
    main()