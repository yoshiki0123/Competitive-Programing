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
    n, x = map(int,input().split())
    while n != 0 or x != 0:
        count = 0
        num = list(range(1,n+1))
        ptns = combinations(num, 3)

        for ptn in ptns:
            total = sum(ptn)
            if total == x:
                count += 1

        print(count)
        n, x = map(int,input().split())
    

if __name__ == '__main__':
    main()