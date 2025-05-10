#library
import sys, re, heapq
from math import ceil, floor, sqrt, isqrt, pi, gcd, comb
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
    N, M = map(int,input().split())
    A = list(map(int, input().split(' ')))
    
    A_minus = []
    for e in A:
        A_minus.append(-e)
    
    heapq.heapify(A_minus)

    for i in range(M):
        X = heapq.heappop(A_minus)
        X /= 2
        X = int(X)
        heapq.heappush(A_minus, X)
    
    ans = (-1) * sum(A_minus)
    print(ans)

    
    
    

if __name__ == '__main__':
    main()