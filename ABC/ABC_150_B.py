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
    S = input().rstrip('\n')
    cur = 0
    while cur < N - 2:
        if S[cur:cur + 3] == 'ABC':
                ans += 1
                cur += 3
        cur +=1

    print(ans)

if __name__ == '__main__':
    main()