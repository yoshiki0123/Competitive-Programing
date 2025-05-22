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
def nCr_mod(n, r, mod):
    """
    n, r, mod を引数とし、nCr を mod で割った余りを返す関数
    """
    # 分子
    numerator = 1
    for i in range(n - r + 1, n + 1):
        numerator *= i
        numerator %= mod
    # 分母
    denominator = 1
    for i in range(1, r + 1):
        denominator *= i
        denominator %= mod
    # モジュラ逆元
    denominator_inv = pow(denominator, -1, mod)
    return numerator * denominator_inv % mod



#main
def main():
    N, a, b = map(int,input().split())
    mod = 10**9+7

    ans = pow(2, N, mod)
    ans -= 1
    ans -= nCr_mod(N, a, mod)
    ans -= nCr_mod(N, b, mod)
    ans %= mod
    print(ans)
    
    

if __name__ == '__main__':
    main()