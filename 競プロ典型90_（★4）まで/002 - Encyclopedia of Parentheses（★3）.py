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
def isvalid(s):
    score = 0
    for c in list(s):
        if c == '(':
            score += 1
        else:
            score -= 1
        if score < 0:
            return False
    if score == 0:
        return True
    else:
        return False
    
#main
def main():
    N = int(input())
    for bit in range(1 << N):
        s = ''
        for i in range(N):
            if bit & (1 << i):
                s += ')'
            else:
                s += '('
        if isvalid(s):
            print(s)
        
if __name__ == '__main__':
    main()