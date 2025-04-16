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
    N = int(input())
    rice_cake_kinds = set()
    for _ in range(N):
        rice_cake_kinds.add(int(input()))
    
    print(len(rice_cake_kinds))


if __name__ == '__main__':
    main()