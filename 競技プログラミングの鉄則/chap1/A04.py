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
def base_n(num_10, n):
    """
    10 進数の整数を n 進数表記の整数へ変換する。
    例：13 -> 1101

    Parameters:
        num_10 (int): 10 進数の整数。
        n (int): 基数 (2 ≦ n ≦ 10)。

    Returns:
        int: n 進数で表した整数。
             基数 n が 10 未満でない桁が生じる場合は -1 を返す。
    """
    if num_10 == 0:
        return 0

    str_n = ''
    while num_10:
        digit = num_10 % n
        if digit >= 10:
            return -1  # n > 10 に対応しない簡易実装
        str_n += str(digit)
        num_10 //= n

    return str_n[::-1]
#main
def main():
    N = int(input())
    print(base_n(N, 2).zfill(10))
    

if __name__ == '__main__':
    main()