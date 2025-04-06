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

    # 座標を格納
    point = []
    for _ in range(N):
        xy = list(map(int, input().split(' ')))
        point.append(xy)
    
    num = list(range(N))
    ptns = list(permutations(num))
    sum_length = 0

    for ptn in ptns:
        for i in range(len(ptn) - 1):
            x1 = point[ptn[i]][0]
            y1 = point[ptn[i]][1]
            x2 = point[ptn[i+1]][0]
            y2 = point[ptn[i+1]][1]

            length = sqrt((x1 - x2)**2 + (y1 - y2)**2)
            sum_length += length
    
    print(sum_length / len(ptns))

if __name__ == '__main__':
    main()


