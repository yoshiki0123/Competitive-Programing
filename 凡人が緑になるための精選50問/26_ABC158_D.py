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
    S = deque(input())
    Q = int(input())
    swap_status = False

    for _ in range(Q):
        line = input().split()
        if line[0] == '1':
            if swap_status == False:
                swap_status = True
            else:
                swap_status = False
        elif line[0] == '2':
            if line[1] == '1':
                if swap_status == False:
                    S.appendleft(line[2])
                else:
                    S.append(line[2])
            else:
                if swap_status == False:
                    S.append(line[2])
                else:
                    S.appendleft(line[2])
    
    if swap_status == False:
        ans = ''.join(S)
        print(ans)
    else:
        ans = ''.join(reversed(S))
        print(ans)


if __name__ == '__main__':
    main()