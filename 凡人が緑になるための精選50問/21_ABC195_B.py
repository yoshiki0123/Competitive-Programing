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
    A, B, W = map(int,input().split())

    min_x = 0
    max_x = 0

    for x in range(10**6 + 1):
        if A*x <= 1000*W and 1000*W <= B*x:
            if min_x == 0:
                min_x = x
            
            max_x = x
    
    if min_x == 0 and max_x == 0:
        print('UNSATISFIABLE')
    else:
        print(min_x, max_x)

    
    

if __name__ == '__main__':
    main()