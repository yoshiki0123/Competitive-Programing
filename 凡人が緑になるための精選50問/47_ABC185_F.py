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
def segfunc(x, y):
    return x ^ y

class SegTree:
    def __init__(self, x_list, init, segfunc):
        """
        セグメント木の初期化
        
        Parameters:
            x_list : 初期配列
            init   : 単位元
            segfunc: 区間クエリに使用する二項演算関数
        """
        self.init = init
        self.segfunc = segfunc
        self.Height = len(x_list).bit_length() + 1
        self.Tree = [init] * (2 ** self.Height)
        self.num = 2 ** (self.Height - 1)

        for i in range(len(x_list)):
            self.Tree[self.num + i] = x_list[i]

        for i in range(self.num - 1, 0, -1):
            self.Tree[i] = segfunc(self.Tree[2 * i], self.Tree[2 * i + 1])

    def select(self, k):
        """k番目の値を取得"""
        return self.Tree[k + self.num]

    def update(self, k, x):
        """k番目の値をxに更新"""
        i = k + self.num
        self.Tree[i] = x
        while i > 1:
            if i % 2 == 0:
                self.Tree[i // 2] = self.segfunc(self.Tree[i], self.Tree[i + 1])
            else:
                self.Tree[i // 2] = self.segfunc(self.Tree[i - 1], self.Tree[i])
            i //= 2

    def query(self, l, r):
        """区間[l, r]のXORを取得 (0-based, r含む)"""
        result = self.init
        l += self.num
        r += self.num + 1
        while l < r:
            if l % 2 == 1:
                result = self.segfunc(result, self.Tree[l])
                l += 1
            if r % 2 == 1:
                result = self.segfunc(result, self.Tree[r - 1])
            l //= 2
            r //= 2
        return result

#def

#main
def main():
    N, Q = map(int,input().split())
    A = list(map(int, input().split(' ')))
    
    seg = SegTree(A, 0, segfunc)

    for i in range(Q):
        T, X, Y = map(int,input().split())

        if T == 1:
            X -= 1
            seg.update(X, seg.select(X)^Y)
        else:
            X -= 1
            Y -= 1
            print(seg.query(X, Y))
        
    
    

if __name__ == '__main__':
    main()