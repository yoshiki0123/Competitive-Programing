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
def lcm(A, B):
    return A*B // gcd(A, B)


#main
def main():
    A, B = map(int,input().split())
    ans = lcm(A, B)
    print(ans)  

if __name__ == '__main__':
    main()
    