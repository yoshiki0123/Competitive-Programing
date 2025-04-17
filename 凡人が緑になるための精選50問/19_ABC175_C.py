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
    X, K, D = map(int,input().split())
    X = abs(X)

    if X >= K*D:
        print(X - K*D)
    else:
       rest_count = K - (X // D)
       if rest_count % 2 == 0:
           print(X - (X // D)*D)
       else:
           print(abs(X - (X // D)*D - D))
           
if __name__ == '__main__':
    main()