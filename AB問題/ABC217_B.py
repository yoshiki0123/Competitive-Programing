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
    names = {'ABC':True, 'ARC':True, 'AGC':True, 'AHC':True}

    for _ in range(3):
        s = input()
        for key in names.keys():
            if s == key:
                names[key] = False
    
    for key, value in names.items():
        if value:
            print(key)


    


if __name__ == '__main__':
    main()