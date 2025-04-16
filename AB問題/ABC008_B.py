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
    vote_result = {}

    for _ in range(N):
        s = input()
        vote_result[s] = vote_result.get(s, 0) + 1
    
    max_value = 0
    ans = ''
    for key, value in vote_result.items():
        if max_value < value:
            max_value = value
            ans = key
    
    print(ans)


if __name__ == '__main__':
    main()