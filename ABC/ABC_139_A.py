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
    T = input().rstrip('\n')
    for i in range(3):
        if S[i] == T[i]:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()