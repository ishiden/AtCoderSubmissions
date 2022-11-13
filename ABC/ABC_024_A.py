import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    A, B, C, K = map(int, input().split())
    S, T = map(int, input().split())
    ans = S * A + T * B
    if S + T >= K:
        ans -= (S+T)*C
    print(ans)

if __name__ == '__main__':
    main()