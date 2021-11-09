import sys
import collections
import heapq
import itertools
import math

input = sys.stdin.readline

def main():
    ans = 'Yes'
    N = int(input())
    S = input().rstrip('\n')
    if S[N-1] == 'x':
        ans = 'No'

    print(ans)

if __name__ == '__main__':
    main()