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
def calc_or(left, right, A):
    res = 0
    for num in A[left:right]:
        res = res | num
    return res

#main
def main():
    N = int(input())
    A = list(map(int, input().split(' ')))

    ans = INF
    for bit in range(1<<(N+1)):
        if bit & 1 == 0 or (bit>>N) & 1 == 0:
            continue
        partition = []
        for shift in range(N+1):
            if (bit>>shift) & 1:
                partition.append(shift)
        
        tmp_ans = 0
        for i in range(len(partition)-1):
            left = partition[i]
            right = partition[i+1]
            tmp_ans ^= calc_or(left, right, A)

        ans = min(ans, tmp_ans)

    print(ans)

if __name__ == '__main__':
    main()