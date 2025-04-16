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
    able_num = set()

    for a in range(2, 10**5 + 1):
        for b in range(2, 33):
            if a**b <= N:
                able_num.add(a**b)
            else:
                break
    
    print(N - len(able_num))
    

    

if __name__ == '__main__':
    main()