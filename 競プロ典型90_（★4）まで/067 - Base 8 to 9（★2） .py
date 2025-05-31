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
def base_10(num_n, n):
    """
    n 進数で表された整数を 10 進数に変換する。

    Parameters:
        num_n (int | str): n 進数で表された数（各桁は 0 ≦ d < n）。
        n (int): 基数。

    Returns:
        int: 10 進数に変換した結果。
    """
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10

def base_n(num_10, n):
    """
    10 進数の整数を n 進数表記の整数へ変換する。

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

    return int(str_n[::-1])


#main
def main():
    N, K = map(int,input().split())
    num_10 = base_10(N, 8)
    for _ in range(K):
        num_9 = base_n(num_10, 9)
        num_9_list = list(str(num_9))
        for i in range(len(num_9_list)):
            if num_9_list[i] == '8':
                num_9_list[i] = '5'
        num_10 = base_10(int(''.join(num_9_list)), 8)
    
    print(base_n(num_10, 8))

if __name__ == '__main__':
    main()