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
def calculate_expected_value(p):
    return (1 + p)*10 / 2

#main
def main():
    N, K = map(int,input().split())
    ps = list(map(int,input().split()))
    total_expected_value = 0
    

    for p in ps[0:K]:
        total_expected_value += calculate_expected_value(p)
    
    ans = total_expected_value

    for i in range(N-K):
        total_expected_value = total_expected_value - calculate_expected_value(ps[i]) + calculate_expected_value(ps[i+K])

        if total_expected_value >= ans:
            ans = total_expected_value

    print(ans / 10)

    

if __name__ == '__main__':
    main()