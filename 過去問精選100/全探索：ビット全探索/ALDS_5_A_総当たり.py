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
    N = int(input())
    A = list(map(int, input().split(' ')))
    Q = int(input())
    M = list(map(int, input().split(' ')))

    
    answer_set = set()
    for i in range(1 << N):
        answer = 0
        for j in range(N):
            if i & (1 << j):
                answer += A[j]
        answer_set.add(answer)
    
    for element in M:
        if element in answer_set:
            print('yes')
        else:
            print('no')        

if __name__ == '__main__':
    main()


