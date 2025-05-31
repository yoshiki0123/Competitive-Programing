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
    H, W = map(int,input().split())
    grid = [list(map(int, input().split(' '))) for _ in range(H)]
    row_totals = []
    col_totals = []

    for i in range(H):
        row_total = sum(grid[i])
        row_totals.append(row_total)
    
    for j  in range(W):
        col_total = sum(grid[i][j] for i in range(H))
        col_totals.append(col_total)

    ans = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            row_i_total = row_totals[i]
            col_j_total = col_totals[j]
            ans[i][j] = row_i_total + col_j_total - grid[i][j]
    
    for i in range(H):
        print(*ans[i])
     

if __name__ == '__main__':
    main()