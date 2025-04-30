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
    ans = 0
    i = 1
    while i*i <= 2*N:     
        if 2 * N % i == 0:         
            x = i         
            y = 2 * N // i         
            if x % 2 != y % 2:             
                ans += 2     
        i += 1
    print(ans)

if __name__ == '__main__':
    main()