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
    N, M = map(int,input().split())
    count = (N+1) * [0]
    for i in range(1, M+1):
        a, b = map(int,input().split())
        if a > b:
            count[a] += 1
        else:
            count[b] += 1
    
    ans = 0
    for count_num in count:
        if count_num == 1:
            ans += 1
    print(ans)
    

if __name__ == '__main__':
    main()