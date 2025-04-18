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
    S = input()
    Q = int(input())
    
    S = list(S)
    swap_status = False

    for _ in range(Q):
        T, A, B = map(int,input().split())
        A -= 1
        B -= 1

        if T == 1:
            if swap_status:
                if A < N and B < N:
                    S[A+N], S[B+N] = S[B+N], S[A+N]

                elif A < N and N <= B:
                    S[A+N], S[B-N] = S[B-N], S[A+N]

                elif N <= A and N <= B:
                    S[A-N], S[B-N] = S[B-N], S[A-N]

            else:
                S[A], S[B] = S[B], S[A]
        
        elif T == 2:
            if swap_status:
                swap_status = False
            else:
                swap_status = True

    if swap_status:
        ans = S[N:] + S[:N]
        ans = ''.join(ans)
        print(ans)   
    else:
        ans = ''.join(S)
        print(ans) 


if __name__ == '__main__':
    main()