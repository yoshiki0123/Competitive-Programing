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
    K = int(input())
    ans = 7 % K
    for i in range(1, K+1):
        if ans == 0:
            print(i)
            exit()
        else:
            ans = (ans*10 + 7) % K
    
    print(-1)

if __name__ == '__main__':
    main()