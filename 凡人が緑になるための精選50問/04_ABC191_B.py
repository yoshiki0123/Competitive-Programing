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
    N, X = map(int,input().split())
    A = list(map(int, input().split(' ')))
    answer = []

    for i in range(N):
        if A[i] != X:
            answer.append(A[i])

    print(*answer)

if __name__ == '__main__':
    main()