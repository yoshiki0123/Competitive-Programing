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
    names = set()

    for _ in range(N):
        S, T = input().split()
        names.add((S, T))
    
    if len(names) == N:
        print('No')
    else:
        print('Yes')
    
    
    

if __name__ == '__main__':
    main()