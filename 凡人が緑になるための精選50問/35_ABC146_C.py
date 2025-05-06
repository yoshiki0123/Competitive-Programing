#library
import sys, re
from math import ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

#class

#def
def price(A, B, N):
    N_str = str(N)
    d = len(N_str)
    
    return A*N + B*d

#main
def main():
    A, B, X = map(int,input().split())
    
    if X < price(A, B, 1):
        print(0)
        exit()
    
    ok = 1 # N = 1
    ng = 10** 20 # N= 10**20
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if price(A, B, mid) <= X:
            ok = mid
        
        else:
            ng = mid
    
    if ok > 10**9:
        print(10**9)
    else:
        print(ok)
    

if __name__ == '__main__':
    main()