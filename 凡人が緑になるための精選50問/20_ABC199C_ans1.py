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
    S = list(input())
    before_S = S[:N]
    after_S = S[N:]
    Q = int(input())
    swap_flg = 0 # 0:通常　1:入れ替え
    swap_count = 0

    for _ in range(Q):
        T, A, B = map(int,input().split())
        A -= 1
        B -= 1

        if T == 1:
            # 通常
            if swap_flg == 0:
                if A < N and B < N:
                    tmp = before_S[A]
                    before_S[A] = before_S[B]
                    before_S[B] = tmp

                elif A < N and B >= N:
                    tmp = before_S[A]
                    before_S[A] = after_S[B-N]
                    after_S[B-N] = tmp
                
                elif A >= N and B >= N:
                    tmp = after_S[A-N]
                    after_S[A-N] = after_S[B-N]
                    after_S[B-N] = tmp
            # 入れ替え
            elif swap_flg ==1:
                if A < N and B < N:
                    tmp = after_S[A]
                    after_S[A] = after_S[B]
                    after_S[B] = tmp

                elif A < N and B >= N:
                    tmp = after_S[A]
                    after_S[A] = before_S[B-N]
                    before_S[B-N] = tmp
                
                elif A >= N and B >= N:
                    tmp = before_S[A-N]
                    before_S[A-N] = before_S[B-N]
                    before_S[B-N] = tmp
                
        elif T == 2:
            swap_count += 1
            if swap_flg == 1:
                swap_flg =0
            else:
                swap_flg = 1    

    if swap_count % 2 == 0:
        ans = before_S + after_S
        ans = ''.join(ans)
        print(ans)    
    else:
        ans = after_S + before_S
        ans = ''.join(ans)
        print(ans)

if __name__ == '__main__':
    main()