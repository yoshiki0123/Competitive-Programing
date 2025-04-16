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
    N = int(input())
    MOD = 10**9 + 7
    A = [x % MOD for x in list(map(int, input().split(' ')))]
    sum_A = sum(A)
    total = 0

    for i in range(N):
        sum_A -= A[i]
        total += A[i] * sum_A
    
    print(total % MOD)
        



    
    

if __name__ == '__main__':
    main()