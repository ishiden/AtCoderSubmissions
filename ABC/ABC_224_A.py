import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 0
    S = input().rstrip('\n')
    if S[-1] == 'r':
        ans = 'er'
    else:
        ans = 'ist'
    print(ans)

if __name__ == '__main__':
    main()