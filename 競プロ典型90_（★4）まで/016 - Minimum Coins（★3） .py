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
    A, B, C = map(int,input().split())
    ans = 10000
    for i in range(10000):
        for j in range(10000):
            value = i * A + j * B
            if N < value or (N - value) % C !=0:
                continue
            res = i + j + (N - value) // C
            if ans > res:
                ans = res
    print(ans)    


    

if __name__ == '__main__':
    main()