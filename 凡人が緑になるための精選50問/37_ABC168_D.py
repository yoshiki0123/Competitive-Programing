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
    N, M = map(int,input().split())
    connect = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, input().split())
        connect[A].append(B)
        connect[B].append(A)

    que = deque()
    visited_places = set()
    guideposts = [-1] * (N+1)

    visited_places.add(1)
    guideposts[1] = 1
    que.append(1)
    
    while que:
        now = que.popleft()
        for to in connect[now]:
            if guideposts[to] == -1:
                visited_places.add(to)
                guideposts[to] = now
                que.append(to)

    if len(guideposts[2:]) == N-1:
        print("Yes")
        for i in range(2, N+1):
            print(guideposts[i])
    
    else:
        print("No")
    

if __name__ == '__main__':
    main()