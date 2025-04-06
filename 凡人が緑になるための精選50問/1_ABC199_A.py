#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#def

#main
def main():
    A, B, C = map(int, input().split())
    if A**2 + B**2 < C**2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()