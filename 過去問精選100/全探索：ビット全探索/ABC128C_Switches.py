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
    N, M = map(int,input().split())
    switchs_list = []
    for _ in range(M):
        parts = list(map(int, input().split()))
        k = parts[0]
        switchs_list.append(parts[1:])
    
    p = list(map(int, input().split()))

    comb = 0
    for i in range(1 << N): # スイッチの状態
        is_all_on = True
        for j in range(M):
            on_switch_num = 0
            swhitchs = switchs_list[j]
            for switch in swhitchs:
                if i & (1 << switch - 1):
                    on_switch_num += 1
            
            if on_switch_num % 2 != p[j]:
                is_all_on = False
                break

        if is_all_on:        
            comb += 1
    
    print(comb)

if __name__ == '__main__':
    main()

