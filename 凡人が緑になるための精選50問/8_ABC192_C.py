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
def g1(x):
    x = list(str(x))
    x.sort(reverse=True)
    x = "".join(x)

    return int(x)
    
def g2(x):
    x = list(str(x))
    x.sort()
    x = "".join(x)

    return int(x)

def f(x):
    return g1(x) - g2(x)

#main
def main():
    N, K = map(int,input().split())
    a = N
    for i in range(K):
        a = f(a)
    
    print(a)
    

if __name__ == '__main__':
    main()