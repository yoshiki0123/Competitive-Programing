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
    N, M, X = map(int,input().split())

    books = []
    for _ in range(N):
        line = list(map(int,input().split()))
        books.append(line)
    
    ans = 12 * 10**6
    for bit in range(1 << N):
        tmp_list = [0] * (M+1)
        for i in range(N):
            if bit & (1 << i):
                for j, e in enumerate(books[i]):
                    tmp_list[j] += e     

        understand_flg = True
        for k in range(1, M+1):
            if tmp_list[k] < X:
                understand_flg = False
        
        if understand_flg:
            ans = min(tmp_list[0], ans)

    if ans == 12 * 10**6:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()