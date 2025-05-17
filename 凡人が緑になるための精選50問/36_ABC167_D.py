#library
import sys, re
from math import ceil, floor, sqrt, isqrt, pi, gcd, comb
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
    N, K = map(int,input().split())
    connect = [None] + list(map(int, input().split()))

    now = 1
    loop_start = 1
    initial = [1]
    loop = []
    visited = {now}

    for i in range(2, N+1):
        next = connect[now]
        if next in visited:
            loop_start = next
            break
        else:
            initial.append(next)
            visited.add(next)
        now = next
    
    for j in range(len(initial)):
        if initial[j] == loop_start:
            loop = initial[j:]
            break
    
    if K < len(initial):
        print(initial[K])
    else:
        print(loop[((K-len(initial)) % len(loop))])


    
    
    

if __name__ == '__main__':
    main()