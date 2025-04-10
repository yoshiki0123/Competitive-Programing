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
def generate_divisors(N):
    divisors = []

    i = 1
    while i**2 <= N:
        if N % i == 0:
            divisors.append(i)
            if i != N // i:
                divisors.append(N // i)
        i += 1

    divisors.sort()
    return divisors

#main
def main():
    N = int(input())
    
    divisors = generate_divisors(N)
    
    for divisor in divisors:
        print(divisor)

if __name__ == '__main__':
    main()