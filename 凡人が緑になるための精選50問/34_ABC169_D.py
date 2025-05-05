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
def prime_factorize(n):
    """
    素因数分解：整数 n を素因数分解して、素因数のリストを返す。

    Parameters:
        n (int): 分解する整数

    Returns:
        list[int]: n を素因数分解した結果のリスト（重複あり、昇順）
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            factors.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        factors.append(n)
    return factors

def solv_quadratic_equation(a, b, c):
    """ 2次方程式を解く  """
    D = b**2 - 4*a*c
    if D < 0:
        return 0, 0  # 虚数解なら何も返さない

    sqrt_D = sqrt(D)
    x1 = (-b + sqrt_D) / (2*a)
    x2 = (-b - sqrt_D) / (2*a)
    return (x1, x2)

def a(index):
    """指数から計算回数を求める"""
    x_1, x_2 = solv_quadratic_equation(float(1) , float(1) , float(2*index))
    return floor(max(x_1, x_2))
    


#main
def main():
    N = int(input())
    factors = prime_factorize(N)
    prime_factor_count = Counter(factors)
    ans = 0

    for value in prime_factor_count.values():
        ans += a(value)

if __name__ == '__main__':
    main()