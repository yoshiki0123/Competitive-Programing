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
    AB_list = []

    for _ in range(N):
        A, B = (map(int,input().split()))
        AB_list.append([A, B])

    AB_list.sort()    

    current_pos = 0

    for A, B in AB_list:
        next_pos = A
        if next_pos - current_pos > K:
            current_pos += K
            print(current_pos)
            exit()
        else:
            K -= (next_pos - current_pos)
            current_pos = next_pos
            K += B
            # print(f'current_pos:{current_pos},K:{K}')
    
    if K > 0:
        current_pos += K

    print(current_pos)

if __name__ == '__main__':
    main()



