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

def to_base_n(x, n):
    """
    10進数の入力xをn進数に変換する関数
    """
    s = ''
    while x > 0:
        s = str(x % n) + s
        x //= n
    
    return int(s)

def has_7(x :int):
    x = str(x)
    if '7' in x:
        return True
    else:
        return False
            
#main
def main():
    N = int(input())
    count = 0
    for num in range(1, N+1):
        # 10進数判定
        if has_7(num):
            count += 1
        else:
            # 8進数変換
            num = to_base_n(num, 8)
            # 8進数判定
            if has_7(num):
                count += 1
    
    print(N - count)
    
    

if __name__ == '__main__':
    main()