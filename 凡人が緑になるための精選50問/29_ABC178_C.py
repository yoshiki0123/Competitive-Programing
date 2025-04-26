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
    N = int(input())
    mod = 10**9 + 7
    ans = (10**N % mod) - ((2 * 9**N - 8**N) % mod)
    print(ans % mod)
    

if __name__ == '__main__':
    main()