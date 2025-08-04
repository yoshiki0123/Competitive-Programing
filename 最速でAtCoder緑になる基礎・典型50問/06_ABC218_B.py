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
    P = list(map(int, input().split(' ')))
    ans = ''

    for i in P:
        ans += chr(i - 1 + ord('a'))

    print(ans)

if __name__ == '__main__':
    main()