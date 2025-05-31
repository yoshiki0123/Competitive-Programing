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
    H, N = map(int,input().split())
    dp = [INF] * (H+1)
    dp[0] = 0

    for i in range(N):
        A, B = map(int,input().split())
        for h in range(H+1):
            if h + A <= H:
                dp[h+A] = min(dp[h+A], dp[h] + B)
            else:
                dp[H] = min(dp[H], dp[h] + B)

    print(dp[H])
        

    
    

if __name__ == '__main__':
    main()