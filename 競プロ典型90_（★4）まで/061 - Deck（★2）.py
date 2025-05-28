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

#main
def main():
    Q = int(input())
    start_deck = []
    end_deck = []
    for _ in range(Q):
        t, x = map(int,input().split())
        if t == 1:
            start_deck.append(x)
        elif t == 2:
            end_deck.append(x)
        else:
            if x <= len(start_deck):
                print(start_deck[-x])
            else:
                x -= len(start_deck)
                print(end_deck[(x-1)])
        
    

if __name__ == '__main__':
    main()