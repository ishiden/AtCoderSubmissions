import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    N = int(input())
    set_s = set()
    score = 0
    for i in range(N):
        S, T = input().split()
        T = int(T)
        if S not in set_s:
            set_s.add(S)
            if score < T:
                ans = i
                score = T
    print(ans+1)

if __name__ == '__main__':
    main()