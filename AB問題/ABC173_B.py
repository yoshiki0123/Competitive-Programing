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
    judge_dict = {'AC':0, 'WA':0, 'TLE':0, 'RE':0}

    for _ in range(N):
        S = input()
        judge_dict[S] += 1
    
    for key, value in judge_dict.items():
        print(f'{key} x {value}')

if __name__ == '__main__':
    main()