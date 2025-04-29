#library
import sys, re
from math import ceil, floor, sqrt, isqrt, pi, gcd, comb
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
    R, S, P = map(int,input().split())
    T = list(input())

    ans = 0
    hand_record = []
    for hand in T[:K]:
        if hand == 'r':
            ans += P
            hand_record.append('p')
            continue
        if hand == 's':
            ans += R
            hand_record.append('r')
            continue
        if hand == 'p':
            ans += S
            hand_record.append('s')
            continue
        

    for hand in T[K:]:
        if hand == 'r':
            if hand_record[-K] != 'p':
                ans += P
                hand_record.append('p')
                continue
        if hand == 's':
            if hand_record[-K] != 'r':
                ans += R
                hand_record.append('r')
                continue
        if hand == 'p':
            if hand_record[-K] != 's':
                ans += S
                hand_record.append('s')
                continue
        hand_record.append('$')
    
    print(ans)
    
        
if __name__ == '__main__':
    main()