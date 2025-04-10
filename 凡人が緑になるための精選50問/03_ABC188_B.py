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
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))

    answer = 0
    for i in range(N):
        answer += A[i] * B[i]
    
    if answer == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()