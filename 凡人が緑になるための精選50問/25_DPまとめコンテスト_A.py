#library
import sys, re
from math import ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#def

#main
def main():
    N = int(input())
    h = [0] + list(map(int, input().split()))
    dp = [10**15] * (N+1)

    dp[1] = 0
    dp[2] = abs(h[1] - h[2]) 

    for i in range(3, N+1):
        cost1 = dp[i-1] + abs(h[i-1] - h[i])
        cost2 = dp[i-2] + abs(h[i-2] - h[i])
        dp[i] =  min(cost1, cost2)  
    
    print(dp[N])

if __name__ == '__main__':
    main()