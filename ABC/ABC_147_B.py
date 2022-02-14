import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 0
    S = input().rstrip('\n')
    p = len(S) // 2
    for i in range(p):
        if S[i] != S[-(i + 1)]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()