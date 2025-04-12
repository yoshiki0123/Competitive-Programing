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
    N, X = map(int,input().split())
    ingestion_quantity = 0

    for i in range(1, N+1):
        V, P = map(int,input().split())
        ingestion_quantity += V * P
        if X * 100 < ingestion_quantity:
            print(i)
            exit()
    
    print(-1)

if __name__ == '__main__':
    main()