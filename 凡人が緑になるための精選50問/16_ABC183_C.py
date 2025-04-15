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
    N, K = map(int,input().split())
    towns = []
    for _ in range(N):
        T = list(map(int, input().split(' ')))
        towns.append(T)

    num = list(range(2, N + 1))
    ptns = list(permutations(num))
    count = 0
    
    for ptn in ptns:
        ptn = (1,) + ptn + (1,)
        dist = 0
        for i in range(len(ptn)-1):
            current_town = ptn[i]
            next_town = ptn[i+1]
            dist += towns[current_town-1][next_town-1]
        
        if dist == K:
            count += 1
    
    print(count)

if __name__ == '__main__':
    main()