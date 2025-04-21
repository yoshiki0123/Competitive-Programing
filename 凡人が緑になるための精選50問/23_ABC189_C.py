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
    A = list(map(int, input().split()))

    ans = -10**15

    for l in range(N):
        A_min = A[l]
        for r in range(l, N):
            A_min = min(A_min, A[r])
            ans = max(ans, A_min * (r - l + 1))
    
    print(ans)


if __name__ == '__main__':
    main()