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
    point = []
    for _ in range(N):
        x, y = map(int,input().split())
        point.append([x, y])

    items = list(range(N))
    for comb in combinations(items, 3):
        x1, y1 = point[comb[0]]
        x2, y2 = point[comb[1]]
        x3, y3 = point[comb[2]]

        # 直線の式：(y - y1)(x2 -x1) = (y2 - y1)(x - x1)
        
        if (y3 - y1)*(x2 -x1) == (y2 - y1)*(x3 - x1):
            print('Yes')
            exit()
    
    print('No')

if __name__ == '__main__':
    main()