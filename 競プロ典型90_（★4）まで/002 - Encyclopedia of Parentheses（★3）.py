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
# カッコ列 S が整合しているかどうか
def isvalid(s):
    score = 0
    for c in list(s):
        if c == '(':
            score += 1
        else:
            score -= 1
        # 途中で0を下回るとFalse    
        if score < 0:
            return False
    # 最後に0ならTrue、そうでなければFalse
    return score == 0
    
#main
def main():
    N = int(input())
    # ()列を順に列挙
    for bit in range(1 << N):
        s = ''
        # 最上位桁から順に見ていく　0 -> '(' , 1 -> ')'
        for i in range(N-1, -1, -1):
            if bit & (1 << i):
                s += ')'
            else:
                s += '('
        if isvalid(s):
            print(s)
        
if __name__ == '__main__':
    main()