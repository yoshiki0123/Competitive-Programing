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
def find_midpoint(x1, y1, x2, y2):
    """
    二点(x1, y1), (x2, y2)の中点を求める関数
    """
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    return midpoint_x, midpoint_y

def rotate_point(x, y, angle):
    """
    座標(x, y)を原点を中心に、angleだけ反時計回りに回転させる関数
    """
    # 角度をラジアンに変換
    theta = radians(angle)
    # 回転行列の適用
    x_new = x * cos(theta) - y * sin(theta)
    y_new = x * sin(theta) + y * cos(theta)
    return x_new, y_new

#main
def main():
    N = int(input())
    x0, y0 = map(int,input().split())
    xN2, yN2 = map(int,input().split())

    mid_x, mid_y = find_midpoint(x0, y0, xN2, yN2)

    # 原点に平行移動後に回転
    x_new, y_new = rotate_point(x0 - mid_x, y0 - mid_y, 360 / N)

    # 逆平行移動
    x1, y1 = x_new + mid_x, y_new + mid_y

    print(x1, y1)
    
if __name__ == '__main__':
    main()