"""
この問題では、pythonの参照渡しにひっかっかった。
具体的には、tmp_grid = gridで新しいtmp_gridを作ったように見えるが
実際にはgridオブジェクトを指すポインタをコピーしただけで
新しいオブジェクトができているわけではない。
そのため、新しいオブジェクトを作るには
tmp_grid = copy.deepcopy(grid)
とする必要がある。
"""

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
def sharp_count(grid):
    sharp_count = 0
    for row in grid:
        for e in row:
            if e == '#':
                sharp_count += 1
    
    return sharp_count

def paint_row(row_num, grid, W):
    for j in range(W):
        grid[row_num][j] = '$'

def paint_col(col_num, grid, H):
    for i in range(H):
        grid[i][col_num] = '$'

#main
def main():
    H, W, K = map(int,input().split())
    grid = []
    for _ in range(H):
        row = list(input())
        grid.append(row)
    
    ans = 0
    for bit in range(1 << (H+W)):
        tmp_grid = grid
        print(bin(bit))
        print(tmp_grid)
        for i in range(H+W):
            if bit & (1 << i):
                #　行の処理
                if i < H: 
                    row_num = i
                    print('row_num', row_num)
                    paint_row(row_num, tmp_grid, W) 
                # 列の処理        
                else: 
                    col_num = i - H
                    print('col_num', col_num)
                    paint_col(col_num, tmp_grid, H)
        print(tmp_grid)
        
        if sharp_count(tmp_grid) == K:
            ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()