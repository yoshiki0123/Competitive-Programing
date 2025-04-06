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
    N, S, D = map(int,input().split())
    for _ in range(N):
        X, Y = map(int,input().split())
        if X < S and Y > D:
            print('Yes')
            exit()
            
    print('No')
    

        
    

if __name__ == '__main__':
    main()