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
    digits = [int(d) for d in str(N)]
    
    max_count = 0
    for i in range(1 << len(digits)):
        total = 0
        count = 0
        for j in range(len(digits)):
            if i & (1 << j):
                total += digits[j]
                count += 1
        
        if total % 3 == 0:
            if max_count < count:
                max_count = count

    if max_count:
        print(len(digits) - max_count)
    else:
        print(-1)

if __name__ == '__main__':
    main()