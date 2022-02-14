import collections
import itertools
import math
import re
import sys
import heapq

input = sys.stdin.readline

def main():
    ans = 'No'
    N = int(input())
    S = input().rstrip('\n')
    c = N // 2
    if S[:c] == S[c:]:
        ans = 'Yes'

    print(ans)

if __name__ == '__main__':
    main()