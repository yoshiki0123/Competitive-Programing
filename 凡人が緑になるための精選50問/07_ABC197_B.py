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
    H, W, X, Y = map(int,input().split())
    X -= 1
    Y -= 1
    grid = []
    for i in range(H):
        S = list(input())
        grid.append(S)

    answer = 1

    # 左
    x, y = X, Y - 1
    while y >= 0:
        if grid[x][y] == '.':
            answer += 1
            y -= 1
        else:
            break

    # 上
    x, y = X - 1, Y
    while x >= 0:
        if grid[x][y] == '.':
            answer += 1
            x -= 1
        else:
            break

    # 右
    x, y = X, Y + 1
    while y <= W - 1:
        if grid[x][y] == '.':
            answer += 1
            y += 1
        else:
            break

    # 下
    x, y = X + 1, Y 
    while x <= H - 1:
        if grid[x][y] == '.':
            answer += 1
            x += 1
        else:
            break
    
    print(answer)
    

if __name__ == '__main__':
    main()