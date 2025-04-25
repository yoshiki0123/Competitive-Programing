#library
import sys, re
from math import ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#def

#main
def main():
    N, M = map(int,input().split())
    #　行けるところリスト
    connect = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int,input().split())
        connect[A].append(B)
    
    
    ans = set()

    for i in range(1, N+1):
        ans.add((i, i))
        que = deque()
        visited = [False] * (N+1)
        start = i
        que.append(i)
        visited[i] = True

        while que:
            now = que.popleft()
            for to in connect[now]:
                if visited[to] == False:
                    visited[to] = True
                    que.append(to)
                    ans.add((start, to))
    
    print(len(ans))

if __name__ == '__main__':
    main()