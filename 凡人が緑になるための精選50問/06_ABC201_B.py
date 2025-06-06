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
    mountains = []
    for _ in range(N):
        S, T = map(str, input().split())
        T = int(T)
        mountains.append([T, S])

    # 二次元配列のソートは、先頭の要素に沿って並び替えられる。
    # sortはO(NlogN)
    mountains.sort(reverse=True) 
    print(mountains[1][1])

if __name__ == '__main__':
    main()