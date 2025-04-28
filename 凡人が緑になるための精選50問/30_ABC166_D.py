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
    X = int(input())
    for A in range(-10**3,10**3):     
        for B in range(-10**3,10**3):         
            if A**5-B**5==X:             
                print(A,B)             
                exit()

if __name__ == '__main__':
    main()