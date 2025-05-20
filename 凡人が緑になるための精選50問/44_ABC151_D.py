#library
import sys, re, heapq
from math import sin, cos, radians, ceil, floor, sqrt, isqrt, pi, gcd, comb
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
    H, W = map(int,input().split())
    grid = []
    for i in range(H):
        row = list(input())
        grid.append(row)

    ans = -1
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                que = deque()
                visited = [[False]*W for _ in range(H)]
                visited[i][j] = True
                que.append((i, j, 0))

                while que:
                    cur_i, cur_j, tmp_ans = que.popleft()
                    # 上,下,左,右
                    for delta_i, delta_j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        next_i, next_j = cur_i + delta_i, cur_j + delta_j
                        if 0 <= next_i <= H-1 and 0 <= next_j <= W-1 and visited[next_i][next_j] == False:
                            if grid[next_i][next_j] != '#':
                                visited[next_i][next_j] = True
                                que.append((next_i, next_j, tmp_ans+1))
            
                ans = max(ans, tmp_ans)
    
    print(ans)
    
if __name__ == '__main__':
    main()