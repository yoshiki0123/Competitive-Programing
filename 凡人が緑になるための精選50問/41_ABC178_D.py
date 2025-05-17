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
    S = int(input())
    dp = [0] * (S+1)
    dp[3:6] = [1] * 3

    for i in range(6, S+1):
        dp[i] = sum(dp[3:i-3+1]) + 1
    
    print(dp[S] % (10**9+7))

    
if __name__ == '__main__':
    main()